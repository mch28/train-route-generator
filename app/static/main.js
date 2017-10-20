$(document).ready(function() {
	console.log("ready");
	

	// $("form").on("submit", function() {
	// 	console.log("form has been submitted")
	$('button').click(function(){
		console.log("function working");
		
		$.ajax({
			url: '/get_data/',
			type: 'POST',
			success: function(resp){
				$('div#response').append(resp.data);
			}
		})
		
	// 	var val2 = $('input[name="number2').val()
		
		 // 	$.ajax({

			// type: "POST",
			// url: "/get_data/",
			// //data: {first: testpt1, second: testpt2},
			// success: function(resp) {
			// 	console.log(results);
			// 	$('div#response').append(resp.data);
			// },
			// error: function(error) {
			// 	console.log.error;
			// }
		//});

	});

	

	// });

	
});