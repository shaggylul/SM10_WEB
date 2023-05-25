//alert("I'm alive")

//a=5
//b=10
//alert(a*b)

//console.log("Привет: ",a*b)

function myfunc(){
	n = document.getElementById("in_name").value;
	a = document.getElementById("in_age").value;
	response=  "Имя: "+n+" Возраст "+a;
	alert(response);
	t = document.getElementById("mytable")
	var row = t.insertRow(4);
	var c_name = row.insertCell(0);
	var c_logo = row.insertCell(1);
	var c_age = row.insertCell(2);
	var c_sum = row.insertCell(3);
	c_name.innerHTML = n;
	c_logo.innerHTML = '<img src="./jokerge.png" width="100" height ="100">';
	c_age.innerHTML = a;
	c_sum.innerHTML = "12";
}