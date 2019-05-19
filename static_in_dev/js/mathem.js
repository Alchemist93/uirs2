const dryLayer1 = document.getElementById('id_dry_layer_thickness_1');
const dryLayer2 = document.getElementById('id_dry_layer_thickness_2');
const dryLayer3 = document.getElementById('id_dry_layer_thickness_3');
const dryLayerOut = document.getElementById('id_dry_layer_thickness_sr');

const primerLayer1 = document.getElementById('id_primer_layer_thickness_1');
const primerLayer2 = document.getElementById('id_primer_layer_thickness_2');
const primerLayer3 = document.getElementById('id_primer_layer_thickness_3');
const primerLayerOut = document.getElementById('id_primer_layer_thickness_sr');

const reverseLayer1 = document.getElementById('id_reverse_layer_thickness_1');
const reverseLayer2 = document.getElementById('id_reverse_layer_thickness_2');
const reverseLayer3 = document.getElementById('id_reverse_layer_thickness_3');
const reverseLayerOut = document.getElementById('id_reverse_layer_thickness_sr');

const brilliance1 = document.getElementById('id_brilliance_1');
const brilliance2 = document.getElementById('id_brilliance_2');
const brilliance3 = document.getElementById('id_brilliance_3');
const brillianceOut = document.getElementById('id_brilliance_sr');

const notchedAdhezion1 = document.getElementById('id_notched_adhesion_1');
const notchedAdhezion2 = document.getElementById('id_notched_adhesion_2');
const notchedAdhezion3 = document.getElementById('id_notched_adhesion_3');
const notchedAdhezionOut = document.getElementById('id_notched_adhesion_sr');

const resToShock1 = document.getElementById('id_resistance_to_shock_1');
const resToShock2 = document.getElementById('id_resistance_to_shock_2');
const resToShock3 = document.getElementById('id_resistance_to_shock_3');
const resToShockOut = document.getElementById('id_resistance_to_shock_sr');

const resAbrasion1 = document.getElementById('id_abrasion_resistance_1');
const resAbrasion2 = document.getElementById('id_abrasion_resistance_2');
const resAbrasion3 = document.getElementById('id_abrasion_resistance_3');
const resAbrasionOut = document.getElementById('id_abrasion_resistance_sr');

const penHardness1 = document.getElementById('id_pencil_hardness_1');
const penHardness2 = document.getElementById('id_pencil_hardness_2');
const penHardness3 = document.getElementById('id_pencil_hardness_3');
const penHardnessOut = document.getElementById('id_pencil_hardness_sr');

const eriksen1 = document.getElementById('id_eriksen_1');
const eriksen2 = document.getElementById('id_eriksen_2');
const eriksen3 = document.getElementById('id_eriksen_3');
const eriksenOut = document.getElementById('id_eriksen_sr');

const colorStandart1 = document.getElementById('id_color_standart_1');
const colorStandart2 = document.getElementById('id_color_standart_2');
const colorStandart3 = document.getElementById('id_color_standart_3');
const colorStandartOut = document.getElementById('id_color_standart_sr');

dryLayer1.addEventListener('input', calcDryLayer);
dryLayer2.addEventListener('input', calcDryLayer);
dryLayer3.addEventListener('input', calcDryLayer);

primerLayer1.addEventListener('input', calcPrimerLayer);
primerLayer2.addEventListener('input', calcPrimerLayer);
primerLayer3.addEventListener('input', calcPrimerLayer);

reverseLayer1.addEventListener('input', calcReverseLayer);
reverseLayer2.addEventListener('input', calcReverseLayer);
reverseLayer3.addEventListener('input', calcReverseLayer);

brilliance1.addEventListener('input', calcBrilliance);
brilliance2.addEventListener('input', calcBrilliance);
brilliance3.addEventListener('input', calcBrilliance);

notchedAdhezion1.addEventListener('input', calcNotchedAdhezion);
notchedAdhezion2.addEventListener('input', calcNotchedAdhezion);
notchedAdhezion3.addEventListener('input', calcNotchedAdhezion);

resToShock1.addEventListener('input', calcResToShock);
resToShock2.addEventListener('input', calcResToShock);
resToShock3.addEventListener('input', calcResToShock);

resAbrasion1.addEventListener('input', calcResAbrasion);
resAbrasion2.addEventListener('input', calcResAbrasion);
resAbrasion3.addEventListener('input', calcResAbrasion);

penHardness1.addEventListener('input', calcPenHardness);
penHardness2.addEventListener('input', calcPenHardness);
penHardness3.addEventListener('input', calcPenHardness);

eriksen1.addEventListener('input', calcEriksen);
eriksen2.addEventListener('input', calcEriksen);
eriksen3.addEventListener('input', calcEriksen);

colorStandart1.addEventListener('input', calcColorStandart);
colorStandart2.addEventListener('input', calcColorStandart);
colorStandart3.addEventListener('input', calcColorStandart);

function calcDryLayer(event) {
		console.log('areaRec exec event ', event);
    const t1Value = dryLayer1.value;
    const t2Value = dryLayer2.value;
    const t3Value = dryLayer3.value;
    var result = (Number(t1Value) + Number(t2Value) + Number(t3Value)) / 3;
    dryLayerOut.value = result;
}

function calcPrimerLayer(event) {
		console.log('areaRec exec event ', event);
    const t1Value = primerLayer1.value;
    const t2Value = primerLayer2.value;
    const t3Value = primerLayer3.value;
    var result = (Number(t1Value) + Number(t2Value) + Number(t3Value)) / 3;
    primerLayerOut.value = result;
}

function calcReverseLayer(event) {
		console.log('areaRec exec event ', event);
    const t1Value = reverseLayer1.value;
    const t2Value = reverseLayer2.value;
    const t3Value = reverseLayer3.value;
    var result = (Number(t1Value) + Number(t2Value) + Number(t3Value)) / 3;
    reverseLayerOut.value = result;
}

function calcBrilliance(event) {
		console.log('areaRec exec event ', event);
    const t1Value = brilliance1.value;
    const t2Value = brilliance2.value;
    const t3Value = brilliance3.value;
    var result = (Number(t1Value) + Number(t2Value) + Number(t3Value)) / 3;
    brillianceOut.value = result;
}
function calcNotchedAdhezion(event) {
		console.log('areaRec exec event ', event);
    const t1Value = notchedAdhezion1.value;
    const t2Value = notchedAdhezion2.value;
    const t3Value = notchedAdhezion3.value;
    var result = (Number(t1Value) + Number(t2Value) + Number(t3Value)) / 3;
    notchedAdhezionOut.value = result;
}

function calcResToShock(event) {
		console.log('areaRec exec event ', event);
    const t1Value = resToShock1.value;
    const t2Value = resToShock2.value;
    const t3Value = resToShock3.value;
    var result = (Number(t1Value) + Number(t2Value) + Number(t3Value)) / 3;
    resToShockOut.value = result;
}

function calcResAbrasion(event) {
		console.log('areaRec exec event ', event);
    const t1Value = resAbrasion1.value;
    const t2Value = resAbrasion2.value;
    const t3Value = resAbrasion3.value;
    var result = (Number(t1Value) + Number(t2Value) + Number(t3Value)) / 3;
    resAbrasionOut.value = result;
}

function calcPenHardness(event) {
		console.log('areaRec exec event ', event);
    const t1Value = penHardness1.value;
    const t2Value = penHardness2.value;
    const t3Value = penHardness3.value;
    var result = (Number(t1Value) + Number(t2Value) + Number(t3Value)) / 3;
    penHardnessOut.value = result;
}
function calcEriksen(event) {
		console.log('areaRec exec event ', event);
    const t1Value = eriksen1.value;
    const t2Value = eriksen2.value;
    const t3Value = eriksen3.value;
    var result = (Number(t1Value) + Number(t2Value) + Number(t3Value)) / 3;
    eriksenOut.value = result;
}

function calcColorStandart(event) {
		console.log('areaRec exec event ', event);
    const t1Value = colorStandart1.value;
    const t2Value = colorStandart2.value;
    const t3Value = colorStandart3.value;
    var result = (Number(t1Value) + Number(t2Value) + Number(t3Value)) / 3;
    colorStandartOut.value = result;
}
