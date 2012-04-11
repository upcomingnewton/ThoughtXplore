// JavaScript Document
var check_type = [
{ "type":"email" , "min_":"10" , "max_":"50" },
{ "type":"rollno" , "min_":"4" , "max_":"7" },
{ "type":"name" , "min_":"4" , "max_":"" },
{ "type":"pass" , "min_":"10" , "max_":"" }
]

function checkmail(elem_id,error_id)
{
	
	var val=document.getElementById(elem_id);
	
	for(i=0;i<4;i++){
		if(elem_id==check_type[i].type){
			id_no=i;
			break;
		}
	}
	
	if(chk_email(val) == true){
		if(max_length(val, i) == true){
			var image='<img src="Tick.png" alt="Tick" height="23" width="23" />';
			error_id.innerHTML=image;
			return true;
		}
		else{
			var image='<img src="Cross.png" alt="Cross" height="23" width="23" />';
			error_id.innerHTML=image;
			val.value='';
			val.placeholder='Valid Email Address Please..!';
			return false;
		}
		
	}
	else if(empty(val)==true)
	{
		var image='<img src="Cross.png" alt="Cross" height="23" width="23" />';
		error_id.innerHTML=image;
		val.value='';
		val.placeholder='Email Address Please..!';
		return false;
	}
	else
	{
		var image='<img src="Cross.png" alt="Cross" height="23" width="23" />';
		error_id.innerHTML=image;
		val.value='';
		val.placeholder='Valid Email Address Please..!';
		return false;
	}
}

function checkname(elem_id,error_id)
{
	
	var val=document.getElementById(elem_id);
	
	for(i=0;i<4;i++){
		if(elem_id==check_type[i].type){
			id_no=i;
			break;
		}
	}
	
	if(name(val) == true){
		if(min_length(val, i) == true){
			var image='<img src="Tick.png" alt="Tick" height="23" width="23" />';
			error_id.innerHTML=image;
			return true;
		}
		else{
			var image='<img src="Cross.png" alt="Cross" height="23" width="23" />';
			error_id.innerHTML=image;
			val.value='';
			val.placeholder='Valid Name Please..!';
			return false;
		}
		
	}
	else if(empty(val)==true)
	{
		var image='<img src="Cross.png" alt="Cross" height="23" width="23" />';
		error_id.innerHTML=image;
		val.value='';
		val.placeholder='Name Please..!';
		return false;
	}
	else
	{
		var image='<img src="Cross.png" alt="Cross" height="23" width="23" />';
		error_id.innerHTML=image;
		val.value='';
		val.placeholder='Valid Name Please..!';
		return false;
	}
}

function checkrollno(elem_id,error_id)
{
	
	var val=document.getElementById(elem_id);
	
	for(i=0;i<4;i++){
		if(elem_id==check_type[i].type){
			id_no=i;
			break;
		}
	}
	
	if(numeric(val) == true){
		if(min_length(val, i) == true){
			if(max_length(val,i) == true){
				var image='<img src="Tick.png" alt="Tick" height="23" width="23" />';
				error_id.innerHTML=image;
				return true;
			}
			else{
				var image='<img src="Cross.png" alt="Cross" height="23" width="23" />';
				error_id.innerHTML=image;
				val.value='';
				val.placeholder='Valid Roll Number Please..!';
				return false;
			}
		}
		else{
			var image='<img src="Cross.png" alt="Cross" height="23" width="23" />';
			error_id.innerHTML=image;
			val.value='';
			val.placeholder='Valid Roll Number Please..!';
			return false;
		}
		
	}
	else if(empty(val)==true)
	{
		var image='<img src="Cross.png" alt="Cross" height="23" width="23" />';
		error_id.innerHTML=image;
		val.value='';
		val.placeholder='Roll Number Please..!';
		return false;
	}
	else
	{
		var image='<img src="Cross.png" alt="Cross" height="23" width="23" />';
		error_id.innerHTML=image;
		val.value='';
		val.placeholder='Valid Roll Number Please..!';
		return false;
	}
}

//All of the generic functions here:
function chk_email(val)
{
	var chk_exp= /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/;
	
	if(val.value.match(chk_exp))
	{
		return true;
	}
	else
	{
		return false;
	}
}
function min_length(val,i)
{
	if(val.value.length > parseInt(check_type[i].min_))
	{
		return true;
	}
	else
	{
		return false;
	}
}

function max_length(val,i)
{
	if(val.value.length < parseInt(check_type[i].max_))
	{
		return true;
	}
	else
	{
		return false;
	}
}
function empty(val)
{
	if(val.value.length == 0){
		return true;
	}
	else{
		return false;
	}
}
function numeric(val)
{
	var chk_exp =  /^[0-9]+$/;
	if(val.value.match(chk_exp))
	{
		return true;
	}
	else
	{
		return false;
	}
}
function alphabets(val)
{
	var chk_exp= /^[a-zA-Z]+$/;
	if(val.value.match(chk_exp))
	{
		return true;
	}
	else
	{
		return false;
	}
}
function alpha_numeric(val)
{
	var chk_exp=/^[0-9a-zA-Z]+$/;
	if(val.value.match(chk_exp))
	{
		return true;
	}
	else
	{
		return false;
	}
}
function name(val){
	var chk_exp=/^[/ a-zA-Z]+$/;
	if(val.value.match(chk_exp))
	{
		return true;
	}
	else
	{
		return false;
	}
}