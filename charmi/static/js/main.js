//Inicio del Header
$(document).ready(main);

	var contador = 1;

	function main(){
		$('.menu_bar').click(function(){

		if(contador == 1){
			$('nav').animate({
				left: '0'
			});
			contador =0;
		}
		else {
			contador =1;
			$('nav').animate({
				left: '-100%'
			});
		}

		});
	}


//fin del header


$(document).ready(function(){

	//Objeto para acceder al slider.
	var banner = {

		padre: $('#banner'),
		numeroSlides: $('#banner').children('.slide').length,
		posicion: 1
	}

	banner.padre.children('.slide').first().css({
		'left': 0 
	});

	console.log(banner.padre.children('slide').first());


	var altoBanner = function(){
		//obtengo el alto de la imagen
		var alto = banner.padre.children('.slide').outerHeight();

		banner.padre.css({
			'height': alto + 'px'
		});
		console.log(alto);

	}

	altoBanner();

	$( window ) .resize(function(){
		altoBanner();
	});


	//Boton Siguiente
	$('#banner-next').on('click', function(e){
		e.preventDefault();

		if(banner.posicion < banner.numeroSlides){
			// Nos aseguramos de que las demas slides empiecen desde la derecha.
			banner.padre.children().not('.active').css({
				'left':'200%'
			});

			//Quitamos la clase active y se la ponemos al siguiente elemento. Y lo animamos
			$('#banner .active').removeClass('active').next().addClass('active').animate({
				'left': '0'
			});

			//Animamos el slide anterior para que se desliza hacia la izq.
			$('#banner .active').prev().animate({
				'left': '-200%'
			});

			banner.posicion = banner.posicion + 1;
		}

		else{
			//es slider activo (el ultimo) se anime a la derecha.
			$('#banner .active').animate({
				'left': '-200%'
			});

			//Le decimos a todos los slides que no esten activo vayan a la derecha
			banner.padre.children().not('.active').css({
				'left':'200%'
			});

			//Eliminamos active y se la ponemos al primer elemento
			$('#banner .active').removeClass('active');
			banner.padre.children('.slide').first().addClass('active').animate({
				'left': 0
			});

			banner.posicion = 1;
		}


	});



	//Boton Anterior
	$('#banner-prev').on('click', function(e){
		e.preventDefault();

		if(banner.posicion > 1){

			banner.padre.children().not('.active').css({
				'left': '-200%'
			});
	
			$('#banner .active').animate({
				'left': '200%'
			});

			$('#banner .active').removeClass('active').prev().addClass('active').animate({
				'left': 0
			});

			banner.posicion = banner.posicion -1;
		}

		else{

			//Le decimos a todos los slides que no esten activo vayan a la derecha
			banner.padre.children().not('.active').css({
				'left':'-200%'
			});


			//es slider activo (el ultimo) se anime a la derecha.
			$('#banner .active').animate({
				'left': '200%'
			});


			//Eliminamos active y se la ponemos al ultimo elemento
			$('#banner .active').removeClass('active');
			banner.padre.children('.slide').last().addClass('active').animate({
				'left': 0
			});

			banner.posicion = banner.numeroSlides;
		}

	});







	var info = {

		padre: $('#info'),
		numeroSlides: $('#info').children('.slide').length,
		posicion: 1
	}

	//para obtener el primer
	
	info.padre.children('.slide').first().css({
		'left': 0 
	});


	console.log(info.padre.children('slide').first());


	//para calcular el alto necesario
	

	var altoInfo = function(){
		//obtengo el alto de la imagen
		var alto = info.padre.children('.slide').outerHeight();

		info.padre.css({
			'height': alto + 'px'
		});
		console.log(alto);
	}

		altoInfo();

	//para hacer responsive con js
	

	$( window ) .resize(function(){
		altoInfo();
	});



		$('#info-next').on('click', function(e){
		e.preventDefault();

		if(info.posicion < info.numeroSlides){
			// Nos aseguramos de que las demas slides empiecen desde la derecha.
			info.padre.children().not('.active').css({
				'left':'200%'
			});

			//Quitamos la clase active y se la ponemos al siguiente elemento. Y lo animamos
			$('#info .active').removeClass('active').next().addClass('active').animate({
				'left': '0'
			});

			//Animamos el slide anterior para que se desliza hacia la izq.
			$('#info .active').prev().animate({
				'left': '-200%'
			});

			info.posicion = info.posicion + 1;
		}

		else{
			//es slider activo (el ultimo) se anime a la derecha.
			$('#info .active').animate({
				'left': '-200%'
			});

			//Le decimos a todos los slides que no esten activo vayan a la derecha
			info.padre.children().not('.active').css({
				'left':'200%'
			});

			//Eliminamos active y se la ponemos al primer elemento
			$('#info .active').removeClass('active');
			info.padre.children('.slide').first().addClass('active').animate({
				'left': 0
			});

			info.posicion = 1;
		}

	});


	$('#info-prev').on('click', function(e){
		e.preventDefault();

		if(info.posicion > 1){

			info.padre.children().not('.active').css({
				'left': '-200%'
			});
	
			$('#info .active').animate({
				'left': '200%'
			});

			$('#info .active').removeClass('active').prev().addClass('active').animate({
				'left': 0
			});

			info.posicion = info.posicion -1;
		}

		else{

			//Le decimos a todos los slides que no esten activo vayan a la derecha
			info.padre.children().not('.active').css({
				'left':'-200%'
			});


			//es slider activo (el ultimo) se anime a la derecha.
			$('#info .active').animate({
				'left': '200%'
			});


			//Eliminamos active y se la ponemos al ultimo elemento
			$('#info .active').removeClass('active');
			info.padre.children('.slide').last().addClass('active').animate({
				'left': 0
			});

			info.posicion = info.numeroSlides;
		}

	});


});