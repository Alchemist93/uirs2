console.log('Test log');
const formOneT1Input = document.getElementById('id_dry_layer_thickness_1');
const formOneT2Input = document.getElementById('id_dry_layer_thickness_2');
const formOneT3Input = document.getElementById('id_dry_layer_thickness_3');
const formOneResInput = document.getElementById('id_dry_layer_thickness_sr');
console.log('formOneT1Input ', formOneT1Input);
console.log('formOneT2Input ', formOneT2Input);
console.log('formOneT3Input ', formOneT3Input);
console.log('formOneResInput ', formOneResInput);

/* document.getElementsByName(document.form1.t1).addEventListener('input', areaRec);
document.getElementsByName(document.form1.t2).addEventListener('input', console.log('123'));
document.getElementsByName(document.form1.t3).addEventListener('input', areaRec); */
formOneT1Input.addEventListener('input', calcArea);
formOneT2Input.addEventListener('input', calcArea);
formOneT3Input.addEventListener('input', calcArea);

function calcArea(event) {
		console.log('areaRec exec event ', event);
    const t1Value = formOneT1Input.value;
    const t2Value = formOneT2Input.value;
    const t3Value = formOneT3Input.value;
    console.log('input values ', { t1Value, t2Value, t3Value });
/*     var a=document.form1.t1.value;
    var b=document.form1.t2.value;
    var c=document.form1.t2.value; */
    var result = (Number(t1Value) + Number(t2Value) + Number(t3Value)) / 3;
    console.log('result ', result);
    formOneResInput.value = result;
}

