# -*- coding: utf-8 -*-
import copy, html, uuid, shutil, zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(".")
SHELL_ZIP = ROOT / "Test_ExportFile_81374.202621_--PRUEBA (2doParcial)-(Cap 7 y 8) NUEVAS Preguntas para PRIMER PARCIAL.--- 12 preguntas totales---a EFs ) Oto2026.zip"
WORK = ROOT / "work"
ORIGINAL = WORK / "original"

CAP7_TITLE = "Capítulo 7 - Causas y soluciones de conflictos en organizaciones familiares (12 preguntas)"
CAP8_TITLE = "Capítulo 8 - Impacto de la práctica del perdón en las organizaciones familiares (12 preguntas)"

cap7 = [
("Según el modelo de dos círculos, ¿qué ocurre con el área de conflicto cuando se separan los subsistemas de empresa y familia?",
 ["Se incrementa proporcionalmente","Permanece igual","Desaparece por completo","Se reduce"],3),
("¿Cuál es una de las principales causas de conflicto en las empresas familiares que, a su vez, genera múltiples conflictos adicionales?",
 ["La confusión entre los subsistemas de empresa y familia","La falta de capital financiero","La competencia del mercado externo","La ausencia de tecnología moderna"],0),
("Según Gimeno et al. (2004), la visión en las empresas familiares, en comparación con las no familiares, tiende a ser:",
 ["Más enfocada en la expansión internacional","Idéntica en términos de rentabilidad","Menos economicista, con mayor peso de objetivos no económicos","Más agresiva en estrategias de crecimiento"],2),
("La analogía de la \"cachucha\" (gorro) mencionada en el capítulo ilustra:",
 ["La necesidad de comportarse congruentemente según la dimensión (familiar o empresa) en que se esté","La importancia de vestir formalmente en la empresa","La jerarquía que deben respetar los empleados","La tradición de usar uniformes en negocios familiares"],0),
("¿Cuál de las siguientes NO es una causa de conflicto derivada de la confusión entre empresa y familia?",
 ["Juego de roles inadecuados dentro de la empresa","Remuneraciones inadecuadas basadas solo en parentesco","Estructuras organizacionales inadecuadas","Luchas de poder por el control de la compañía"],3),
("El documento llamado \"protocolo familiar\" tiene como función principal:",
 ["Establecer los precios de los productos de la empresa","Regular las actividades recreativas de la familia","Definir los lineamientos sobre asuntos empresariales que competen a la familia, como la incorporación de parientes","Servir como contrato de compraventa de acciones"],2),
("La analogía del arquero que apunta a la estrella versus el que apunta directamente al blanco ilustra la importancia de:",
 ["Tener metas realistas y alcanzables","Crear una visión sublime e inspiradora, por encima de lo modesto","Evitar cualquier tipo de planeación","Competir agresivamente contra otras empresas"],1),
("Según el capítulo, la \"descripción de trayectorias\" (plan de vida y carrera) en una empresa familiar sirve para:",
 ["Garantizar un puesto vitalicio a cada miembro familiar","Reducir la incertidumbre proyectando el desarrollo de cada miembro, sin ser una garantía de puesto","Eliminar la necesidad de capacitación externa","Asignar salarios fijos de por vida a los familiares"],1),
("En una empresa familiar de segunda generación, dos hermanos con responsabilidades muy diferentes reciben exactamente el mismo salario. El hermano con mayor carga de trabajo muestra desmotivación creciente. Según los conceptos del capítulo, ¿cuál es el diagnóstico más preciso de esta situación?",
 ["Es una práctica correcta porque el valor supremo de la familia es el amor y la igualdad entre hermanos","El problema es exclusivamente de comunicación, no de remuneración","Debería resolverse simplemente despidiendo al hermano menos productivo","Se está aplicando lógica del sistema familiar (igualdad) al sistema empresarial, lo cual desmotiva a los más rentables y comprometidos"],3),
("Una empresa familiar enfrenta una crisis económica severa. Los hermanos que dirigen distintas áreas comienzan a culparse mutuamente y buscan aliados entre otros familiares. Según las ideas del capítulo, ¿cuál sería la combinación más efectiva de estrategias para manejar esta situación?",
 ["Encapsular el conflicto entre los involucrados directos y que el líder promueva mentalidad positiva y unión en momentos de crisis","Ignorar el conflicto y esperar que la crisis pase naturalmente","Escalar el conflicto al consejo familiar para que vote por un ganador","Separar definitivamente a los hermanos creando empresas independientes"],0),
("Caso Rick y Dick Hoyt: La historia de este equipo padre-hijo se presenta al final del capítulo sobre conflictos. ¿Cuál es la conexión temática más profunda entre este caso y el contenido del capítulo?",
 ["Demuestra que las personas con discapacidad no deben trabajar en empresas familiares","Es un ejemplo de cómo los conflictos deportivos se resuelven mejor que los empresariales","Ilustra cómo la comunicación profunda y el trabajo en equipo entre padre e hijo pueden superar cualquier limitación, reforzando la idea de que la familia puede ser una fortaleza cuando hay visión compartida","Muestra que el éxito solo depende del esfuerzo físico individual"],2),
("Caso Rick y Dick Hoyt: Dick es descrito como \"el cuerpo\" y Rick como \"el corazón\" del equipo. Si trasladamos esta metáfora a una empresa familiar donde un padre fundador (operativo) trabaja con un hijo (estratégico/visionario) que tiene limitaciones para la ejecución diaria, ¿cuál sería la lección aplicable según los principios del capítulo?",
 ["El hijo debería ser excluido de la empresa porque no puede ejecutar tareas operativas","Cada miembro aporta valor de forma diferente; la clave es reconocer y aprovechar las fortalezas complementarias, definiendo roles claros y una visión compartida","El padre debería retirarse para dejar al hijo a cargo de todo","No hay relación posible entre el caso deportivo y una empresa familiar"],1),
]

cap8 = [
("Según Robert Enright, el perdón se define como:",
 ["El acto de olvidar completamente el daño recibido","Minimizar los actos dañinos de otra persona","El deseo de abandonar el resentimiento y fomentar compasión hacia quien nos lastimó injustamente","Un autosacrificio donde se reprimen los sentimientos negativos"],2),
("¿Cuál de las siguientes afirmaciones sobre el perdón es correcta según el capítulo?",
 ["Perdonar es sinónimo de olvidar","Perdonar ocurre de un momento a otro como decisión instantánea","Perdonar implica necesariamente volver a la situación inicial con la persona","Perdonar no significa tolerar la ineficiencia ni disminuir el nivel de exigencia en las organizaciones"],3),
("Las tres dimensiones del perdón según el Dr. Enright son:",
 ["Afectiva, cognitiva y de actitud","Económica, social y política","Física, mental y espiritual","Individual, grupal y organizacional"],0),
("¿Cuál es el orden correcto de las fases del proceso de curación (perdón)?",
 ["Indignación → Víctima → Negación → Autoculpa → Integración → Supervivencia","Negación → Autoculpa → Víctima → Indignación → Supervivencia → Integración","Autoculpa → Negación → Supervivencia → Víctima → Integración → Indignación","Víctima → Indignación → Negación → Autoculpa → Supervivencia → Integración"],1),
("La ley de reciprocidad de Gouldner (1960) aplicada al perdón establece que:",
 ["Quien recibe daño debe responder con el mismo nivel de agresión","Las relaciones familiares siempre son recíprocas en lo económico","El perdón solo funciona si ambas partes actúan simultáneamente","Quien recibe un beneficio (como el perdón) adquiere el precepto moral de retribuir al donante"],3),
("La \"tríada del perdón\" está compuesta por:",
 ["Otorgamiento del perdón, solicitud del perdón y perdón a uno mismo","Perdón afectivo, cognitivo y conductual","Perdón familiar, empresarial y social","Perdón inmediato, perdón gradual y perdón definitivo"],0),
("La diferencia fundamental entre perdonar a otros y perdonarse a uno mismo radica en:",
 ["El tiempo que toma cada proceso","La cantidad de energía emocional invertida","El tema de la reconciliación: al perdonarse a uno mismo, la reconciliación debe ser parte del perdón","No hay diferencia, ambos son procesos idénticos"],2),
("En el estudio de Park y Enright (1997), ¿qué hallazgo clave se encontró sobre la disposición para perdonar?",
 ["Solo las personas religiosas son capaces de perdonar","Existe gran correlación entre la disposición para perdonar y la comprensión de lo que significa el perdón","La edad es el único factor determinante para perdonar","Las mujeres perdonan más fácilmente que los hombres"],1),
("La parábola de los dos monjes y la dama ilustra metafóricamente que:",
 ["Los monjes no deben interactuar con mujeres bajo ninguna circunstancia","Las reglas religiosas siempre deben respetarse literalmente","Es mejor no ayudar a desconocidos para evitar conflictos","Cargar resentimientos innecesariamente es más dañino que el acto original que los provocó"],3),
("Un padre fundador regañó públicamente a su hijo frente a todos los empleados. El hijo decide dejar de hablarle \"para que se percate del daño.\" Según los conceptos del capítulo sobre las leyes de igualdad y reciprocidad, ¿qué análisis es más preciso?",
 ["El hijo está respondiendo con la ley de igualdad negativa (\"me dañas, te daño\"), lo cual mantiene abierta la herida; el perdón generaría una respuesta de reciprocidad positiva del padre","El hijo actúa correctamente porque debe establecer límites claros con su padre","El conflicto se resolvería solo con el tiempo sin necesidad de ninguna acción","El hijo debería escalar el conflicto al consejo de administración"],0),
("Caso Don Aurelio García: Ernesto abandonó el restaurante que su suegro financió, generando pérdidas de aproximadamente un millón de dólares. Ahora pide apoyo nuevamente. Según los conceptos del capítulo, ¿cuál de las siguientes afirmaciones refleja mejor la aplicación del perdón en este caso?",
 ["Perdonar a Ernesto obliga a Don Aurelio a invertir de nuevo porque perdonar es volver a la situación inicial","No se puede perdonar a Ernesto porque el daño económico fue demasiado grande","Don Aurelio puede perdonar a Ernesto (liberándose del rencor) y aun así decidir no invertir nuevamente si no le conviene financieramente","El perdón solo aplica entre padres e hijos, no entre suegros y yernos"],2),
("Caso Don Aurelio García: La familia está dividida — Ricardo y Joaquín se oponen terminantemente, mientras doña Margarita y María Guadalupe creen que hay que olvidar y apoyar. Integrando los conceptos de la tríada del perdón, las fases de curación y las leyes de reciprocidad, ¿cuál sería la recomendación más integral para Don Aurelio?",
 ["Debe votar la familia democráticamente y acatar la decisión mayoritaria, ya que el perdón es un acto colectivo","Debe separar la decisión emocional (proceso de perdón personal) de la decisión empresarial (inversión); avanzar en su propio proceso de curación evaluando si ha superado la fase de indignación, y evaluar la inversión con criterios de negocio independientes, considerando que Ernesto ha mostrado señales de arrepentimiento genuino (condición para recibir perdón según Enright)","Debe rechazar la solicitud definitivamente porque ya le dio una oportunidad y el daño fue irreversible","Debe esperar otros 10 años hasta que el proceso de curación se complete naturalmente"],1),
]

def set_html_text(el, text, size="12.0pt"):
    el.text = f'&lt;p&gt;&lt;span style="font-size:{size};"&gt;{html.escape(text)}&lt;/span&gt;&lt;/p&gt;'

def mk_feedback(ident):
    fb = ET.Element("itemfeedback", {"ident":"%s"%ident, "view":"All"})
    flow1 = ET.SubElement(fb, "flow_mat", {"class":"Block"})
    flow2 = ET.SubElement(flow1, "flow_mat", {"class":"FORMATTED_TEXT_BLOCK"})
    material = ET.SubElement(flow2, "material")
    ext = ET.SubElement(material, "mat_extension")
    ET.SubElement(ext, "mat_formattedtext", {"type":"HTML"})
    return fb

def build_item(i, q):
    question, options, correct_idx = q
    item = ET.Element("item", {"ident":f"ITEM_{uuid.uuid4().hex}","title":f"Pregunta {i}","maxattempts":"0"})
    md = ET.SubElement(item, "itemmetadata")
    fields = [
        ("bbmd_asi_object_id", f"_{33000000+i}_1"), ("bbmd_asitype","Item"), ("bbmd_assessmenttype","Test"),
        ("bbmd_sectiontype","Subsection"), ("bbmd_questiontype","Multiple Choice"), ("bbmd_is_from_cartridge","false"),
        ("bbmd_is_disabled","false"), ("bbmd_negative_points_ind","N"), ("bbmd_canvas_fullcrdt_ind","false"),
        ("bbmd_all_fullcredit_ind","false"), ("bbmd_numbertype","letter_lower"), ("bbmd_partialcredit","false"),
        ("bbmd_orientationtype","vertical"), ("bbmd_is_extracredit","false"),
    ]
    for k,v in fields:
        ET.SubElement(md, k).text = v
    ET.SubElement(md, "bbmd_is_metadataenabled")
    ET.SubElement(md, "bbmd_ai_state").text = "No"
    ET.SubElement(md, "qmd_absolutescore_max").text = "10.000000000000000"
    ET.SubElement(md, "qmd_weighting").text = "0"
    ET.SubElement(md, "qmd_instructornotes")

    pres = ET.SubElement(item, "presentation")
    flow = ET.SubElement(pres, "flow", {"class":"Block"})
    qblk = ET.SubElement(flow, "flow", {"class":"QUESTION_BLOCK"})
    qfmt = ET.SubElement(qblk, "flow", {"class":"FORMATTED_TEXT_BLOCK"})
    qmat = ET.SubElement(qfmt, "material")
    qext = ET.SubElement(qmat, "mat_extension")
    qtxt = ET.SubElement(qext, "mat_formattedtext", {"type":"HTML"})
    set_html_text(qtxt, question, "14.0pt")

    rblk = ET.SubElement(flow, "flow", {"class":"RESPONSE_BLOCK"})
    rl = ET.SubElement(rblk, "response_lid", {"ident":"response","rcardinality":"Single","rtiming":"No"})
    rc = ET.SubElement(rl, "render_choice", {"shuffle":"Yes","minnumber":"0","maxnumber":"0"})

    option_ids = []
    for opt in options:
        oid = f"OPT_{uuid.uuid4().hex}"
        option_ids.append(oid)
        fl = ET.SubElement(rc, "flow_label", {"class":"Block"})
        label = ET.SubElement(fl, "response_label", {"ident":oid,"shuffle":"Yes","rarea":"Ellipse","rrange":"Exact"})
        fm = ET.SubElement(label, "flow_mat", {"class":"FORMATTED_TEXT_BLOCK"})
        mat = ET.SubElement(fm, "material")
        ext = ET.SubElement(mat, "mat_extension")
        txt = ET.SubElement(ext, "mat_formattedtext", {"type":"HTML"})
        set_html_text(txt, opt, "12.0pt")

    rp = ET.SubElement(item, "resprocessing", {"scoremodel":"SumOfScores"})
    out = ET.SubElement(rp, "outcomes")
    ET.SubElement(out, "decvar", {"varname":"SCORE","vartype":"Decimal","defaultval":"0","minvalue":"0","maxvalue":"10.00000"})
    c = ET.SubElement(rp, "respcondition", {"title":"correct"})
    cv = ET.SubElement(c, "conditionvar")
    ET.SubElement(cv, "varequal", {"respident":"response","case":"No"}).text = option_ids[correct_idx]
    ET.SubElement(c, "setvar", {"variablename":"SCORE","action":"Set"}).text = "SCORE.max"
    ET.SubElement(c, "displayfeedback", {"linkrefid":"correct","feedbacktype":"Response"})

    w = ET.SubElement(rp, "respcondition", {"title":"incorrect"})
    cv2 = ET.SubElement(w, "conditionvar")
    ET.SubElement(cv2, "other")
    ET.SubElement(w, "setvar", {"variablename":"SCORE","action":"Set"}).text = "0"
    ET.SubElement(w, "displayfeedback", {"linkrefid":"incorrect","feedbacktype":"Response"})

    item.append(mk_feedback("correct"))
    item.append(mk_feedback("incorrect"))
    return item

def write_xml(path, tree):
    ET.indent(tree, space="  ")
    tree.write(path, encoding="UTF-8", xml_declaration=True)

def build_res00002(template_tree, title, questions):
    root = copy.deepcopy(template_tree.getroot())
    assessment = root.find("assessment")
    assessment.set("title", title)
    for p in [
        "rubric/flow_mat/material/mat_extension/mat_formattedtext",
        "presentation_material/flow_mat/material/mat_extension/mat_formattedtext",
    ]:
        el = assessment.find(p)
        if el is not None:
            el.text = f"&lt;p&gt;{html.escape(title)}&lt;/p&gt;"

    section = assessment.find("section")
    for old in list(section.findall("item")):
        section.remove(old)
    for i, q in enumerate(questions, start=1):
        section.append(build_item(i, q))
    return ET.ElementTree(root)

def package(folder_name, title, questions):
    out = ROOT / folder_name
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(ORIGINAL, out)

    man = ET.parse(out / "imsmanifest.xml")
    res = man.getroot().find('.//resource[@identifier="res00002"]')
    res.set("{http://www.blackboard.com/content-packaging/}title", title)
    write_xml(out / "imsmanifest.xml", man)

    template = ET.parse(ORIGINAL / "res00002.dat")
    new_res = build_res00002(template, title, questions)
    write_xml(out / "res00002.dat", new_res)

    zpath = ROOT / f"{folder_name}.zip"
    if zpath.exists():
        zpath.unlink()
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(out.rglob("*")):
            arc = str(p.relative_to(out))
            if p.is_dir():
                zf.writestr(arc.rstrip("/") + "/", "")
            else:
                zf.write(p, arcname=arc)
    return zpath

def main():
    if WORK.exists():
        shutil.rmtree(WORK)
    ORIGINAL.mkdir(parents=True)
    with zipfile.ZipFile(SHELL_ZIP) as zf:
        zf.extractall(ORIGINAL)

    print(package("bb_capitulo_7", CAP7_TITLE, cap7))
    print(package("bb_capitulo_8", CAP8_TITLE, cap8))

if __name__ == "__main__":
    main()
