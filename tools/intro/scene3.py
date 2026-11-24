import bpy, addon_utils, math, os, time
from mathutils import Vector, Matrix
addon_utils.enable('io_curve_svg')
D = os.environ.get('CC_DIR', '/Users/reillymitchell/Movies/CaptCan-Intro') + '/'
if bpy.app.background:
    bpy.ops.wm.read_factory_settings(use_empty=True)
else:
    for o in list(bpy.data.objects): bpy.data.objects.remove(o, do_unlink=True)
sc = bpy.context.scene

def imp(svg):
    before = set(bpy.data.objects)
    bpy.ops.import_curve.svg(filepath=D + svg)
    objs = [o for o in bpy.data.objects if o not in before]
    for o in objs:
        if o.name not in sc.collection.objects: sc.collection.objects.link(o)
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs: o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.object.join()
    ob = bpy.context.active_object
    for sp in ob.data.splines:
        for pt in sp.bezier_points: pt.radius = 1.0
    return ob

txt = imp('i3/logo_text.svg'); leaf = imp('i3/logo_leaf.svg')
# common scale: text width -> 8.0 units, centred on the text
TW = 8.0
s = TW / txt.dimensions.x
bpy.ops.object.select_all(action='DESELECT')
for o in (txt, leaf):
    o.scale = (s, s, s)
bpy.context.view_layer.update()
# centre of text bbox in world
def bbox_center(o):
    cs = [o.matrix_world @ Vector(c) for c in o.bound_box]
    return sum(cs, Vector()) / 8
c = bbox_center(txt)
for o in (txt, leaf):
    o.location -= Vector((c.x, c.y, 0))
bpy.context.view_layer.update()

def to_mesh(o, extrude, bevel):
    o.data.extrude = extrude / o.scale.x; o.data.bevel_depth = bevel / o.scale.x; o.data.bevel_resolution = 3
    o.data.materials.clear()
    bpy.ops.object.select_all(action='DESELECT'); o.select_set(True); bpy.context.view_layer.objects.active = o
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.mesh.select_all(action='SELECT'); bpy.ops.mesh.normals_make_consistent(inside=False); bpy.ops.object.mode_set(mode='OBJECT')
    return o
to_mesh(txt, 0.55, 0.01)
to_mesh(leaf, 0.06, 0.008)
leaf.location.z = -0.12

# ---------- materials ----------
def face_mat():
    m = bpy.data.materials.new('Face'); m.use_nodes = True; nt = m.node_tree; b = nt.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (0.92, 0.92, 0.9, 1); b.inputs['Roughness'].default_value = 0.18
    b.inputs['Coat Weight'].default_value = 1.0; b.inputs['Coat Roughness'].default_value = 0.05
    tex = nt.nodes.new('ShaderNodeTexImage'); tex.image = bpy.data.images.load(D + 'i3/pack/art_01.jpg')
    tc = nt.nodes.new('ShaderNodeTexCoord'); mp = nt.nodes.new('ShaderNodeMapping')
    mp.inputs['Scale'].default_value = (1.0, 1.0, 1); mp.inputs['Location'].default_value = (0, 0, 0)
    nt.links.new(tc.outputs['Window'], mp.inputs['Vector']); nt.links.new(mp.outputs['Vector'], tex.inputs['Vector'])
    em = nt.nodes.new('ShaderNodeEmission'); nt.links.new(tex.outputs['Color'], em.inputs['Color']); em.inputs['Strength'].default_value = 1.4
    mix = nt.nodes.new('ShaderNodeMixShader'); mix.inputs['Fac'].default_value = 0.0
    out = nt.nodes['Material Output']
    nt.links.new(em.outputs[0], mix.inputs[1]); nt.links.new(b.outputs[0], mix.inputs[2]); nt.links.new(mix.outputs[0], out.inputs['Surface'])
    return m, tex, mix, mp
FACE, ART, MIX, MAP = face_mat()
side = bpy.data.materials.new('Side'); side.use_nodes = True; sb = side.node_tree.nodes['Principled BSDF']
sb.inputs['Base Color'].default_value = (0.55, 0.012, 0.02, 1); sb.inputs['Roughness'].default_value = 0.22; sb.inputs['Coat Weight'].default_value = 0.8
snt = side.node_tree
wv = snt.nodes.new('ShaderNodeTexWave'); wv.wave_type = 'BANDS'; wv.bands_direction = 'Z'; wv.inputs['Scale'].default_value = 1100; wv.inputs['Distortion'].default_value = 0.0; wv.inputs['Detail'].default_value = 0; wv.wave_profile = 'SAW'
stc = snt.nodes.new('ShaderNodeTexCoord'); snt.links.new(stc.outputs['Generated'], wv.inputs['Vector'])
pr = snt.nodes.new('ShaderNodeValToRGB'); pr.color_ramp.elements[0].color = (0.3, 0.27, 0.23, 1); pr.color_ramp.elements[1].color = (0.95, 0.92, 0.84, 1); pr.color_ramp.elements[1].position = 0.12
snt.links.new(wv.outputs['Fac'], pr.inputs['Fac'])
stex = snt.nodes.new('ShaderNodeTexImage'); stex.image = bpy.data.images.load(D + 'i3/pack/art_05.jpg')
smp = snt.nodes.new('ShaderNodeMapping'); smp.inputs['Scale'].default_value = (3.0, 1.0, 1); snt.links.new(stc.outputs['Generated'], smp.inputs['Vector']); snt.links.new(smp.outputs['Vector'], stex.inputs['Vector'])
paper = snt.nodes.new('ShaderNodeMix'); paper.data_type = 'RGBA'; paper.blend_type = 'MULTIPLY'; paper.inputs['Factor'].default_value = 0.6
snt.links.new(pr.outputs['Color'], paper.inputs[6]); snt.links.new(stex.outputs['Color'], paper.inputs[7])
sidemix = snt.nodes.new('ShaderNodeMix'); sidemix.data_type = 'RGBA'; sidemix.inputs['Factor'].default_value = 0.0
sidemix.inputs[7].default_value = (0.55, 0.012, 0.02, 1)
snt.links.new(paper.outputs[2], sidemix.inputs[6]); snt.links.new(sidemix.outputs[2], sb.inputs['Base Color'])
SIDEMIX = sidemix
txt.data.materials.append(FACE); txt.data.materials.append(side)
# assign: faces pointing +z -> face material (0), everything else side (1)
for p in txt.data.polygons:
    p.material_index = 0 if abs(p.normal.z) > 0.9 else 1
lm = bpy.data.materials.new('Leaf'); lm.use_nodes = True; ln = lm.node_tree; ln.nodes.remove(ln.nodes['Principled BSDF'])
le = ln.nodes.new('ShaderNodeEmission'); le.inputs['Color'].default_value = (0.85, 0.0, 0.02, 1); le.inputs['Strength'].default_value = 0.0
ln.links.new(le.outputs[0], ln.nodes['Material Output'].inputs['Surface']); leaf.data.materials.append(lm)
LEAF_EM = le

# ---------- world / backdrop / lights ----------
world = bpy.data.worlds.new('W'); sc.world = world; world.use_nodes = True
bg = world.node_tree.nodes['Background']; bg.inputs['Color'].default_value = (0.03, 0.002, 0.003, 1); bg.inputs['Strength'].default_value = 1.0
bpy.ops.mesh.primitive_plane_add(size=160, location=(0, 0, -3)); wall = bpy.context.active_object
wm = bpy.data.materials.new('Wall'); wm.use_nodes = True; nt = wm.node_tree; nt.nodes.remove(nt.nodes['Principled BSDF'])
em = nt.nodes.new('ShaderNodeEmission'); gr = nt.nodes.new('ShaderNodeTexGradient'); gr.gradient_type = 'SPHERICAL'
tc = nt.nodes.new('ShaderNodeTexCoord'); mp = nt.nodes.new('ShaderNodeMapping'); mp.inputs['Scale'].default_value = (0.07, 0.12, 1)
ramp = nt.nodes.new('ShaderNodeValToRGB'); ramp.color_ramp.elements[0].color = (0.004, 0.0, 0.0, 1); ramp.color_ramp.elements[1].color = (0.2, 0.003, 0.008, 1)
nt.links.new(tc.outputs['Object'], mp.inputs['Vector']); nt.links.new(mp.outputs['Vector'], gr.inputs['Vector'])
nt.links.new(gr.outputs['Fac'], ramp.inputs['Fac']); nt.links.new(ramp.outputs['Color'], em.inputs['Color'])
nt.links.new(em.outputs['Emission'], nt.nodes['Material Output'].inputs['Surface']); wall.data.materials.append(wm)
WALL_EM = em
def area(loc, rot, size, energy, color=(1, 1, 1)):
    bpy.ops.object.light_add(type='AREA', location=loc, rotation=rot); l = bpy.context.active_object
    l.data.size = size; l.data.energy = energy; l.data.color = color; return l
area((0, 5, 6), (math.radians(-40), 0, 0), 10, 700)
area((-8, -2, 3), (0, math.radians(-65), 0), 5, 420, (1, 0.5, 0.5))
area((8, 2, 3), (0, math.radians(65), 0), 5, 420, (1, 0.9, 0.85))
bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 2, 15)); sbx = bpy.context.active_object
sbx.scale = (30, 8, 1); sbx.rotation_euler = (math.radians(180), 0, 0); sbx.visible_camera = False
sm = bpy.data.materials.new('sb'); sm.use_nodes = True; sn = sm.node_tree; sn.nodes.remove(sn.nodes['Principled BSDF'])
se = sn.nodes.new('ShaderNodeEmission'); se.inputs['Strength'].default_value = 1.4
sn.links.new(se.outputs[0], sn.nodes['Material Output'].inputs['Surface']); sbx.data.materials.append(sm)

bpy.ops.object.camera_add(location=(0, 0, 12)); cam = bpy.context.active_object; sc.camera = cam
cam.data.dof.use_dof = True
sc.render.engine = 'CYCLES'; sc.cycles.device = 'CPU'
try:
    cp = bpy.context.preferences.addons['cycles'].preferences
    cp.compute_device_type = 'METAL'; cp.get_devices()
    for dv in cp.devices: dv.use = True
    sc.cycles.device = 'GPU'; print('GPU', [dv.name for dv in cp.devices], flush=True)
except Exception as e: print('CPU fallback', e, flush=True)
sc.cycles.samples = int(os.environ.get('SAMPLES', 96)); sc.cycles.use_denoising = True
sc.render.resolution_x = int(os.environ.get('RX', 1920)); sc.render.resolution_y = int(os.environ.get('RY', 1080))
sc.view_settings.view_transform = 'AgX'; sc.view_settings.look = 'AgX - Punchy'
sc.render.image_settings.file_format = 'JPEG'; sc.render.image_settings.quality = 92

FPS = 24; DUR = 8.0; N = int(FPS * DUR)
K = [ # t, cam, look, lens, fstop
 (0.0, (-4.6, 0.9, 0.9), (-3.0, 0.0, 0), 28, 1.6),
 (2.6, (-0.6, -1.1, 1.1), (0.6, 0.05, 0), 28, 1.8),
 (4.6, (3.6, 1.3, 2.2), (1.8, 0.0, 0), 32, 2.6),
 (6.6, (0.2, 0.05, 13.0), (0, 0.05, 0), 50, 5.6),
 (8.0, (0, 0.05, 14.2), (0, 0.05, 0), 50, 5.6)]
def ease(x): return x * x * (3 - 2 * x)
def cr(p0, p1, p2, p3, u):
    return 0.5 * ((2 * p1) + (-p0 + p2) * u + (2 * p0 - 5 * p1 + 4 * p2 - p3) * u * u + (-p0 + 3 * p1 - 3 * p2 + p3) * u * u * u)
def at(t):
    i = 0
    for j in range(len(K) - 1):
        if K[j][0] <= t: i = j
    a, b = K[i], K[i + 1]; u = max(0, min(1, (t - a[0]) / (b[0] - a[0]))); ue = ease(u) if i == len(K) - 2 else u
    P = [Vector(K[max(0, min(len(K) - 1, j))][1]) for j in (i - 1, i, i + 1, i + 2)]
    L = [Vector(K[max(0, min(len(K) - 1, j))][2]) for j in (i - 1, i, i + 1, i + 2)]
    return cr(*P, ue), cr(*L, ue), a[3] + (b[3] - a[3]) * ue, a[4] + (b[4] - a[4]) * ue
imgs = [bpy.data.images.load(D + f'i3/pack/art_{k:02d}.jpg') for k in range(1, 25)]
def setframe(t):
    pos, look, lens, fs = at(t)
    cam.location = pos; d = look - pos
    fwd = d.normalized(); up = Vector((0, 1, 0)); right = fwd.cross(up).normalized(); up2 = right.cross(fwd)
    roll = 0.16 * max(0, 1 - t / 5.0); r2 = right * math.cos(roll) + up2 * math.sin(roll); u2 = up2 * math.cos(roll) - right * math.sin(roll)
    cam.rotation_euler = Matrix((r2, u2, -fwd)).transposed().to_euler()
    cam.data.lens = lens; cam.data.dof.focus_distance = d.length; cam.data.dof.aperture_fstop = fs
    rate = 9 if t < 5.4 else (4 if t < 6.4 else 0)
    ART.image = imgs[int(t * rate) % 24] if rate else imgs[0]
    MAP.inputs['Location'].default_value = (0.01 * t, 0.0, 0)
    k = max(0, min(1, (t - 6.0) / 1.4)); k = k * k * (3 - 2 * k)
    MIX.inputs['Fac'].default_value = k                      # art -> white enamel
    LEAF_EM.inputs['Strength'].default_value = 2.2 * max(0, min(1, (t - 6.6) / 0.8)); leaf.hide_render = t < 6.4
    WALL_EM.inputs['Strength'].default_value = 1.0 + 0.2 * k
    SIDEMIX.inputs['Factor'].default_value = k
    sb.inputs['Roughness'].default_value = 0.6 - 0.4 * k
if True:
    out = os.environ.get('OUT', 'frames/'); os.makedirs(D + out, exist_ok=True)
    frames = [int(x) for x in os.environ['FR'].split(',')] if os.environ.get('FR') else range(int(os.environ.get('START', 0)), N, int(os.environ.get('STEP', 1)))
    for fr in frames:
        p = D + out + f'{fr:04d}.jpg'
        if os.path.exists(p) and not os.environ.get('FR'): continue
        setframe(fr / FPS); sc.render.filepath = p
        t0 = time.time(); bpy.ops.render.render(write_still=True); print('F', fr, round(time.time() - t0, 1), flush=True)
