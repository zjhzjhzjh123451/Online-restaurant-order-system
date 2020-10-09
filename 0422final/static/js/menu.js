function getMenu() {
	$.ajax({
        url: "/get_dish",
        dataType : "json",
        success: function(items) {
            
            update_dish_list(items,1);
            update_dish_type(items);
            updating_floatingwindows(items);
            // alert("hui");
        }
    });
}

function hiddeUI(){
	var ui =document.getElementById("cart");
	ui.style.visibility="hidden";

}

function update_dish_type(items){
	var dish_type = JSON.parse(items['dish_type'])
	$("#navbarSupportedContent").empty();
	for (var i = 0; i < dish_type.length; i++) {
		this_type = dish_type[i];
		 	// alert(this_type.fields.typeId);
		$("#navbarSupportedContent").prepend(
			"<div class=\"col-lg-auto col-md-6 text-center\">"+
			"<div class=\"nav-item dropdown\">"+
			"<div class=\"mt-3 mb-3\">"+
			"<h3 class=\"nav-link dropdown-toggle h4 mb-2\" id=\""+this_type.fields.typeId+"\" onclick=\"show(id)\" role=\"button\" data-toggle=\"dropdown\" aria-haspopup=\"true\" aria-expanded=\"false\">"+
			this_type.fields.name+
			"</h3>"+
			"</div>"+
			"</div>"+
			"</div>"
			);
	}
	former_dtypenums = dish_type.length;
}

function update_dish_list(items,value){
	 var dishes = JSON.parse(items['dishes']);
	 dishtypeid = parseInt(value);
	 $(".row.no-gutters").empty();
	 for (var i = 0; i < dishes.length; i++) {
	 	this_dish = dishes[i];

		dish_typeid = parseInt(this_dish.fields.typeid);
		dishname = this_dish.fields.name;
		if (dishname.indexOf(" ") != -1) 
		{	
			const name = dishname.split(" ",3);
			dishname = name[0];

			// alert(name[0]);
		}
	 	if (dish_typeid==dishtypeid) {
	 		if (this_dish.fields.is_selling=='1') {
	 		$(".row.no-gutters").prepend(
	 			"<div class=\"col-lg-4 col-sm-6\">"+
	 			"<a class=\"portfolio-box\" data-toggle=\"modal\" data-target=\"#"+dishname+"_floating\">"+
	 			"<img class=\"img-fluid\" src=\"/get_photo/"+this_dish.fields.dishId+"\"  alt=\"\" />"+
	 			"<div class=\"portfolio-box-caption\">"+
	 			"<div class=\"project-category text-white-50\">"+
	 			this_dish.fields.name+"</div>"+
	 			"</div>"+
	 			"</a>"+
	 			"</div>"
	 		);	
	 		}
	 	}
	 	
	 }

}

function updating_floatingwindows(items) {
	var dishes = JSON.parse(items['dishes']);
	$("#floating_windows").empty();
	for (var i = 0; i < dishes.length; i++) {
		this_dish = dishes[i];
		if (this_dish.fields.is_selling=='1') {
			is_selling="is selling";
		}else{
			is_selling="Sold out";
		}

		if (this_dish.fields.is_recommend=='0') {
			is_recommended = "⭐";
		}
		else if(this_dish.fields.is_recommend=='1'){
			is_recommended = "⭐⭐";
		}
		else{
			is_recommended = "⭐⭐⭐";	
		}

		dishname = this_dish.fields.name;
		if (dishname.indexOf(" ") != -1) 
		{	
			const name = dishname.split(" ",3);
			dishname = name[0];
			// alert(element.innerHTML);
		}

		$("#floating_windows").prepend(
				"<div class=\"modal fade\" id=\"" +dishname+"_floating\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"exampleModalCenterTitle\" aria-hidden=\"true\">"+
				"<div class=\"modal-dialog modal-dialog-centered\" role=\"document\">"+
				"<div class=\"modal-content\">"+
				"<div class=\"modal-header\">"+
				"<h5 class=\"modal-title\" id=\"exampleModalLongTitle\">"+this_dish.fields.name+"</h5>"+
				"<button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\">"+
				"<span aria-hidden=\"true\">"+"x"+"</span>"+
				"</button>"+
				"</div>"+
				"<div class=\"modal-body\">"+
				"<img class=\"img-fluid\" height=\"450\" width=\"450\" src=\"/get_photo/"+this_dish.fields.dishId+"\"  alt=\"\" />"+
				"Dish Description: <a>"+this_dish.fields.description+"</a><br>"+
				"Recommendation Rate: <a>"+is_recommended+"</a><br>"+
				"Surplus: <a>"+is_selling+"</a><br>"+
				"Price: $ <a class=\""+this_dish.fields.name+"\" >"+this_dish.fields.price+"</a>"+
				"</div>"+
				"<div class=\"modal-footer\">"+
				"<div class=\"input-group mb-3\">"+
				"<div class=\"input-group-prepend\">"+
					"<span class=\"input-group-text\" id=\"basic-addon1\">Quantity</span>"+
				"</div>"+
				"<input type=\"text\" class=\"form-control\" disabled=\"disabled\" value=\"0\" aria-label=\"Username\" aria-describedby=\"basic-addon1\" id=\""+this_dish.fields.name+"_quntity\">"+
				"</div>"+
				"<button type=\"button\" class=\"btn btn-secondary\" onclick=\"plus(value)\" value=\""+this_dish.fields.name+"_quntity\">"+"+"+"</button>"+
				"<button type=\"button\" class=\"btn btn-secondary\" onclick=\"minus(value)\"value=\""+this_dish.fields.name+"_quntity\">"+"-"+"</button>"+
				"<button type=\"button\" class=\"btn btn-primary\" data-dismiss=\"modal\" onclick=\"save(value)\"value=\""+this_dish.fields.name+"_quntity\">Save</button>"+
				"</div>"+
				"</div>"+
				"</div>"+
				"</div>"
			);
		

	}

		 former_dishnums = dishes.length;
}

function update_cart(number,name,price){
	int_price = parseInt(price);
	int_number = parseInt(number);
	if (name.indexOf(" ") != -1) 
	{	
		const dishname = name.split(" ",3);
		name = dishname[0];
		// alert(element.innerHTML);
	}
	if (document.getElementById(name)) {
		$("#"+name).remove();
		$("#"+name+"_dish").remove();
		if (int_number!=0) {
		$("#cart_items").prepend(
			"<div class=\"col-lg-1 text-center\" data-toggle=\"modal\" data-target=\"#"+name+"_floating\" id=\""+name+"_dish\">"+
			"<i class=\"fas fa-4x fa-gem text-primary mb-4\"></i>"+
			"<h3 class=\"h4 mb-2\" >"+name+"</h3>"+
			"<p class=\"text-light mb-0\">"+number+"</p>"+
			"</div>"
		);
		$("#cart_form").prepend(
		"<div class=\"col-lg-1 text-center\" id=\""+name+"\">"+
		"<input type=\"hidden\" name=\"dish[]\" value=\""+name+"\">"+
		"<input type=\"hidden\" name=\"num[]\" value=\""+number+"\">"+
		"</div>"
		);
		}
		pre_number = parseInt(cart[name]);
		// alert(cart[name]);
		subtotal_amount = subtotal_amount - pre_number*int_price + int_price*int_number; 
		document.getElementById("subtotal_amount").value = subtotal_amount;
		document.getElementById("sub_amount").innerHTML = '$'+subtotal_amount;
		cart[name] = number;

	} 
	else{
		if (int_number!=0) {
		$("#cart_items").prepend(
			"<div class=\"col-lg-1 text-center\" id=\""+name+"_dish\">"+
			"<i class=\"fas fa-4x fa-gem text-primary mb-4\"></i>"+
			"<h3 class=\"h4 mb-2\" data-toggle=\"modal\" data-target=\"#"+name+"_floating\" >"+name+"</h3>"+
			"<p class=\"text-light mb-0\">"+number+"</p>"+
			"</div>"
		);
		$("#cart_form").prepend(
		"<div class=\"col-lg-1 text-center\" id=\""+name+"\">"+
		"<input type=\"hidden\" name=\"dish[]\" value=\""+name+"\" >"+
		"<input type=\"hidden\" name=\"num[]\" value=\""+number+"\">"+
		"</div>"
		);
		subtotal_amount = subtotal_amount + int_price*int_number;
		// subtotal_amount += '';
		// alert(subtotal_amount);
		document.getElementById("subtotal_amount").value = subtotal_amount;
		document.getElementById("sub_amount").innerHTML = '$'+subtotal_amount;
		// menu.coke = name;
		cart[name] = number;
		}
	}
	if (subtotal_amount==0) {
		hiddeUI();
	}else{
		var ui =document.getElementById("cart");
		ui.style.visibility="visible";
	}
	
}

function plus(value){
	 // alert(value);
	pre_value = document.getElementById(value).value ;
	pre_value = parseInt(pre_value);
	current_value = pre_value+1;
	document.getElementById(value).value = current_value;
}

function minus(value){
	 // alert(value);
	pre_value = document.getElementById(value).value ;
	pre_value = parseInt(pre_value);
	current_value = pre_value-1;
	if (current_value<0) {
		current_value = 0;
	}
	document.getElementById(value).value = current_value;
}

function save(value){
	pre_value = document.getElementById(value).value;
	const name = value.split("_",2);
	var item_price = document.getElementsByClassName(name[0]);
	price = item_price[0].innerHTML;
	// alert(cart.name);
	update_cart(pre_value,name[0],price);
}
function show(value){
	// alert(value);
	$.ajax({
        url: "/get_dish",
        dataType : "json",
        success: function(items) {
            // alert(value);
            update_dish_list(items,value);
            // update_dish_type(items,);
            // updating_floatingwindows(items);
            // alert("hui");
        }
    });
}
window.onload = function(){
	getMenu();
	hiddeUI();

}
var former_dishnums = 0;
var former_dtypenums = 0;
var subtotal_amount = 0;
var cart = {};
// var menu = {};