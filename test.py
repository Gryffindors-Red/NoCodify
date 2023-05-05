<!DOCTYPE html>
<html lang="en">
{% load static %}

<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->

	<title>NoCodify</title>
{% comment %} ==================================================================================================== {% endcomment %}
<link rel="stylesheet" href=" {% static 'css/chat.css' %} ">
<link rel="stylesheet" href=" {% static 'css/home.css' %} ">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
{% comment %} =============================================================================================================================== {% endcomment %}
	<!-- Google font -->
	<link href="https://fonts.googleapis.com/css?family=Montserrat:400,700%7CVarela+Round" rel="stylesheet">

	<!-- Bootstrap -->
	<link type="text/css" rel="stylesheet" href=" {% static 'css/bootstrap.min.css' %} " />
	<link href=
	"https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css"
			  rel="stylesheet">
	<!-- Owl Carousel -->
	<link type="text/css" rel="stylesheet" href=" {% static 'css/owl.carousel.css' %} " />
	<link type="text/css" rel="stylesheet" href=" {% static 'css/Automation.css' %} " />

	<link type="text/css" rel="stylesheet" href=" {% static 'css/owl.theme.default.css' %} " />

	<!-- Magnific Popup -->
	<link type="text/css" rel="stylesheet" href=" {% static 'css/magnific-popup.css' %} " />

	<!-- Font Awesome Icon -->
	<link rel="stylesheet" href=" {% static 'css/font-awesome.min.css' %} ">

	<!-- Custom stlylesheet -->
	<link type="text/css" rel="stylesheet" href=" {% static 'css/style.css' %} " />

	<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
	<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
	<!--[if lt IE 9]>
		<script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
		<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
	<![endif]-->
</head>

<style>
	.container {
		text-align: center;
	  }
	  
	  .glitch {
		font-size: 5rem;
		font-weight: bold;
		text-transform: uppercase;
		position: relative;
		text-shadow: 0.05em 0 0 #00fffc, -0.03em -0.04em 0 #fc00ff,
		  0.025em 0.04em 0 #fffc00;
		animation: glitch 725ms infinite;
	  }
	  
	  .glitch span {
		position: absolute;
		top: 0;
		left: 0;
	  }
	  
	  .glitch span:first-child {
		animation: glitch 500ms infinite;
		clip-path: polygon(0 0, 100% 0, 100% 35%, 0 35%);
		transform: translate(-0.04em, -0.03em);
		opacity: 0.75;
	  }
	  
	  .glitch span:last-child {
		animation: glitch 375ms infinite;
		clip-path: polygon(0 65%, 100% 65%, 100% 100%, 0 100%);
		transform: translate(0.04em, 0.03em);
		opacity: 0.75;
	  }
	  
	  @keyframes glitch {
		0% {
		  text-shadow: 0.05em 0 0 #00fffc, -0.03em -0.04em 0 #fc00ff,
			0.025em 0.04em 0 #fffc00;
		}
		15% {
		  text-shadow: 0.05em 0 0 #00fffc, -0.03em -0.04em 0 #fc00ff,
			0.025em 0.04em 0 #fffc00;
		}
		16% {
		  text-shadow: -0.05em -0.025em 0 #00fffc, 0.025em 0.035em 0 #fc00ff,
			-0.05em -0.05em 0 #fffc00;
		}
		49% {
		  text-shadow: -0.05em -0.025em 0 #00fffc, 0.025em 0.035em 0 #fc00ff,
			-0.05em -0.05em 0 #fffc00;
		}
		50% {
		  text-shadow: 0.05em 0.035em 0 #00fffc, 0.03em 0 0 #fc00ff,
			0 -0.04em 0 #fffc00;
		}
		99% {
		  text-shadow: 0.05em 0.035em 0 #00fffc, 0.03em 0 0 #fc00ff,
			0 -0.04em 0 #fffc00;
		}
		100% {
		  text-shadow: -0.05em 0 0 #00fffc, -0.025em -0.04em 0 #fc00ff,
			-0.04em -0.025em 0 #fffc00;
		}
	  }
	  .chat-bar-collapsible {
		position: fixed;
		bottom: 0;
		right: 50px;
		box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
	}
	
	.collapsible {
		background-color: rgb(82, 151, 255);
		color: white;
		cursor: pointer;
		padding: 18px;
		width: 350px;
		text-align: left;
		outline: none;
		font-size: 18px;
		border-radius: 10px 10px 0px 0px;
		border: 3px solid white;
		border-bottom: none;
	}
	
	.content {
		max-height: 0;
		overflow: hidden;
		transition: max-height 0.2s ease-out;
		background-color: #f1f1f1;
	}
	
	.full-chat-block {
		width: 350px;
		background: white;
		text-align: center;
		overflow: auto;
		scrollbar-width: none;
		height: max-content;
		transition: max-height 0.2s ease-out;
	}
	
	.outer-container {
		min-height: 500px;
		bottom: 0%;
		position: relative;
	}
	
	.chat-container {
		max-height: 500px;
		width: 100%;
		position: absolute;
		bottom: 0;
		left: 0;
		scroll-behavior: smooth;
		hyphens: auto;
	}
	
	.chat-container::-webkit-scrollbar {
		display: none;
	}
	
	.chat-bar-input-block {
		display: flex;
		float: left;
		box-sizing: border-box;
		justify-content: space-between;
		width: 100%;
		align-items: center;
		background-color: rgb(235, 235, 235);
		border-radius: 10px 10px 0px 0px;
		padding: 10px 0px 10px 10px;
	}
	
	.chat-bar-icons {
		display: flex;
		justify-content: space-evenly;
		box-sizing: border-box;
		width: 25%;
		float: right;
		font-size: 20px;
	}
	
	#chat-icon:hover {
		opacity: .7;
	}
	
	/* Chat bubbles */
	
	#userInput {
		width: 75%;
	}
	
	.input-box {
		float: left;
		border: none;
		box-sizing: border-box;
		width: 100%;
		border-radius: 10px;
		padding: 10px;
		font-size: 16px;
		color: #000;
		background-color: white;
		outline: none
	}
	
	.userText {
		color: white;
		font-family: Helvetica;
		font-size: 16px;
		font-weight: normal;
		text-align: right;
		clear: both;
	}
	
	.userText span {
		line-height: 1.5em;
		display: inline-block;
		background: #5ca6fa;
		padding: 10px;
		border-radius: 8px;
		border-bottom-right-radius: 2px;
		max-width: 80%;
		margin-right: 10px;
		animation: floatup .5s forwards
	}
	
	.botText {
		color: #000;
		font-family: Helvetica;
		font-weight: normal;
		font-size: 16px;
		text-align: left;
	}
	
	.botText span {
		line-height: 1.5em;
		display: inline-block;
		background: #e0e0e0;
		padding: 10px;
		border-radius: 8px;
		border-bottom-left-radius: 2px;
		max-width: 80%;
		margin-left: 10px;
		animation: floatup .5s forwards
	}
	
	@keyframes floatup {
		from {
			transform: translateY(14px);
			opacity: .0;
		}
		to {
			transform: translateY(0px);
			opacity: 1;
		}
	}
	
	@media screen and (max-width:600px) {
		.full-chat-block {
			width: 100%;
			border-radius: 0px;
		}
		.chat-bar-collapsible {
			position: fixed;
			bottom: 0;
			right: 0;
			width: 100%;
		}
		.collapsible {
			width: 100%;
			border: 0px;
			border-top: 3px solid white;
			border-radius: 0px;
		}
	}

	html {
		scroll-behavior: smooth;
		font-family: Helvetica, sans-serif, Arial;
	}
	
	body {
		margin: 0 auto;
	}
</style>

<body>
	<!-- Header -->
	<header id="home">
		<!-- Background Image -->
		<div class="bg-img"
			style="background-image: url('https://preview.redd.it/0bb6dqsiab451.gif?s=b0c65596a54a30708da26669da6e79abf3be1680');">
			<div class="overlay"></div>
		</div>
		<!-- /Background Image -->

		<!-- Nav -->
		<nav id="nav" class="navbar nav-transparent">
			<div class="container" style="    display: flex;
			justify-content: space-between;">

				<div class="navbar-header">
					<!-- Logo -->
					<div class="navbar-brand">
						<a href=" {% static 'index.html' %} ">
							<img class="logo" src=" {% static 'img/logo-alt.png' %} " alt="logo">
							<img class="logo-alt" src=" {% static 'img/logo-alt.png' %} " alt="logo">
						</a>
					</div>
					<!-- /Logo -->

					<!-- Collapse nav button -->
					<div class="nav-collapse">
						<span></span>
					</div>

				</div>


				<ul class="main-nav nav navbar-nav navbar-right">
					<li><a href="/home">Home</a></li>
					<li><a href="/home">About</a></li>

					<li><a href="home">Team</a></li>
					<li class="has-dropdown"><a>NoCode</a>
						<ul class="dropdown">
							<li><a href="/add"> Create Page</a></li>
							<li><a href="/view_pages"> View templates</a></li>
						</ul>
					</li>
				
					<li class="has-dropdown"><a>Blog</a>
						<ul class="dropdown">
							<li><a href="/blog_edit"> Create Blog</a></li>
							<li><a href="/list_edit_blog"> Edit Blogs</a></li>
							<li><a href="/list_blog"> list Blogs</a></li>
						</ul>
					</li>

					<li class="has-dropdown"><a>Edit</a>
						<ul class="dropdown">
							<li><a href="/url"> URL</a></li>
						</ul>
					</li>
					</li>
					<li><a href=" {% static '#contact' %} ">MarketPlace</a></li>
					<li><div class="wallet-buttons">
						{% if wallet != 'Your wallet address is the key to unlocking the magic of the blockchain. Connect it now and explore the limitless possibilities!' %}
							<form id="metamask-form" method="POST" action="{% url 'DisConnect' %}" >
								{% csrf_token %}
								<button style="padding: 15px;" id='connectWallet' type="submit" class="text-gray-900 bg-white hover:bg-gray-100 border border-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-gray-600 dark:bg-gray-800 dark:border-gray-700 dark:text-white dark:hover:bg-gray-700 mr-2 mb-2">
									<svg aria-hidden="true" class="w-6 h-5 mr-2 -ml-1" viewBox="0 0 2405 2501" fill="none" xmlns="http://www.w3.org/2000/svg"> <g clip-path="url(#clip0_1512_1323)"> <path d="M2278.79 1730.86L2133.62 2221.69L1848.64 2143.76L2278.79 1730.86Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M1848.64 2143.76L2123.51 1767.15L2278.79 1730.86L1848.64 2143.76Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M2065.2 1360.79L2278.79 1730.86L2123.51 1767.15L2065.2 1360.79ZM2065.2 1360.79L2202.64 1265.6L2278.79 1730.86L2065.2 1360.79Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1890.29 1081.17L2285.34 919.338L2265.7 1007.99L1890.29 1081.17ZM2253.21 1114.48L1890.29 1081.17L2265.7 1007.99L2253.21 1114.48Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M2253.21 1114.48L2202.64 1265.6L1890.29 1081.17L2253.21 1114.48ZM2332.34 956.82L2265.7 1007.99L2285.34 919.338L2332.34 956.82ZM2253.21 1114.48L2265.7 1007.99L2318.65 1052.01L2253.21 1114.48Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1542.24 2024.17L1641 2055.7L1848.64 2143.75L1542.24 2024.17Z" fill="#E2761B" stroke="#E2761B" stroke-width="5.94955"/> <path d="M2202.64 1265.6L2253.21 1114.48L2296.64 1147.8L2202.64 1265.6ZM2202.64 1265.6L1792.71 1130.55L1890.29 1081.17L2202.64 1265.6Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1987.86 617.696L1890.29 1081.17L1792.71 1130.55L1987.86 617.696Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M2285.34 919.338L1890.29 1081.17L1987.86 617.696L2285.34 919.338Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1987.86 617.696L2400.16 570.1L2285.34 919.338L1987.86 617.696Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M2202.64 1265.6L2065.2 1360.79L1792.71 1130.55L2202.64 1265.6Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M2382.31 236.33L2400.16 570.1L1987.86 617.696L2382.31 236.33Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M2382.31 236.33L1558.3 835.45L1547.59 429.095L2382.31 236.33Z" fill="#E2761B" stroke="#E2761B" stroke-width="5.94955"/> <path d="M934.789 380.309L1547.59 429.095L1558.3 835.449L934.789 380.309Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1792.71 1130.55L1558.3 835.449L1987.86 617.696L1792.71 1130.55Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1792.71 1130.55L2065.2 1360.79L1682.65 1403.04L1792.71 1130.55Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M1682.65 1403.04L1558.3 835.449L1792.71 1130.55L1682.65 1403.04Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M1987.86 617.696L1558.3 835.45L2382.31 236.33L1987.86 617.696Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M940.144 2134.24L1134.69 2337.11L869.939 2096.16L940.144 2134.24Z" fill="#C0AD9E" stroke="#C0AD9E" stroke-width="5.94955"/> <path d="M1848.64 2143.75L1940.86 1793.33L2123.51 1767.15L1848.64 2143.75Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M151.234 1157.92L487.978 803.917L194.666 1115.67L151.234 1157.92Z" fill="#E2761B" stroke="#E2761B" stroke-width="5.94955"/> <path d="M2123.51 1767.15L1940.86 1793.33L2065.2 1360.79L2123.51 1767.15ZM1558.3 835.449L1230.48 824.74L934.789 380.309L1558.3 835.449Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M2065.2 1360.79L1940.86 1793.33L1930.74 1582.12L2065.2 1360.79Z" fill="#E4751F" stroke="#E4751F" stroke-width="5.94955"/> <path d="M1682.65 1403.04L2065.2 1360.79L1930.74 1582.12L1682.65 1403.04Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M1230.48 824.74L1558.3 835.449L1682.65 1403.04L1230.48 824.74Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1230.48 824.74L345.784 6.08252L934.79 380.309L1230.48 824.74ZM934.195 2258.58L165.513 2496.56L12.0146 1910.53L934.195 2258.58Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M265.465 1304.27L555.803 1076.41L799.14 1132.93L265.465 1304.27Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M799.139 1132.93L555.803 1076.41L686.098 538.567L799.139 1132.93Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M194.666 1115.67L555.803 1076.41L265.465 1304.27L194.666 1115.67Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1930.74 1582.12L1780.81 1506.56L1682.65 1403.04L1930.74 1582.12Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M194.666 1115.67L169.083 980.618L555.803 1076.41L194.666 1115.67Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1749.88 1676.72L1780.81 1506.56L1930.74 1582.12L1749.88 1676.72Z" fill="#233447" stroke="#233447" stroke-width="5.94955"/> <path d="M1940.86 1793.33L1749.88 1676.72L1930.74 1582.12L1940.86 1793.33Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M555.803 1076.41L169.082 980.618L137.55 866.982L555.803 1076.41ZM686.098 538.567L555.803 1076.41L137.55 866.982L686.098 538.567ZM686.098 538.567L1230.48 824.74L799.139 1132.93L686.098 538.567Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M799.14 1132.93L1230.48 824.74L1422.65 1411.96L799.14 1132.93ZM1422.65 1411.96L826.508 1399.47L799.14 1132.93L1422.65 1411.96Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M265.465 1304.27L799.14 1132.93L826.508 1399.47L265.465 1304.27ZM1682.65 1403.04L1422.65 1411.96L1230.48 824.74L1682.65 1403.04Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1780.81 1506.56L1749.88 1676.72L1682.65 1403.04L1780.81 1506.56Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M345.784 6.08252L1230.48 824.74L686.098 538.567L345.784 6.08252Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M12.0146 1910.53L758.088 1879.59L934.195 2258.58L12.0146 1910.53Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M934.194 2258.58L758.088 1879.59L1124.58 1861.75L934.194 2258.58Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M1749.88 1676.72L1940.86 1793.33L2046.16 2041.42L1749.88 1676.72ZM826.508 1399.47L12.0146 1910.53L265.465 1304.27L826.508 1399.47ZM758.088 1879.59L12.0146 1910.53L826.508 1399.47L758.088 1879.59ZM1682.65 1403.04L1731.43 1580.33L1495.83 1594.02L1682.65 1403.04ZM1495.83 1594.02L1422.65 1411.96L1682.65 1403.04L1495.83 1594.02Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1134.69 2337.11L934.194 2258.58L1631.48 2375.79L1134.69 2337.11Z" fill="#C0AD9E" stroke="#C0AD9E" stroke-width="5.94955"/> <path d="M265.465 1304.27L151.234 1157.91L194.666 1115.67L265.465 1304.27Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1710.61 2288.92L1631.48 2375.79L934.194 2258.58L1710.61 2288.92Z" fill="#D7C1B3" stroke="#D7C1B3" stroke-width="5.94955"/> <path d="M1748.09 2075.93L934.194 2258.58L1124.58 1861.75L1748.09 2075.93Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M934.194 2258.58L1748.09 2075.93L1710.61 2288.92L934.194 2258.58Z" fill="#D7C1B3" stroke="#D7C1B3" stroke-width="5.94955"/> <path d="M137.55 866.982L110.777 409.462L686.098 538.567L137.55 866.982ZM194.665 1115.67L115.536 1035.35L169.082 980.618L194.665 1115.67Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1289.38 1529.76L1422.65 1411.96L1403.61 1699.92L1289.38 1529.76Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M1422.65 1411.96L1289.38 1529.76L1095.43 1630.31L1422.65 1411.96Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M2046.16 2041.42L2009.87 2014.65L1749.88 1676.72L2046.16 2041.42Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1095.43 1630.31L826.508 1399.47L1422.65 1411.96L1095.43 1630.31Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M1403.61 1699.92L1422.65 1411.96L1495.83 1594.02L1403.61 1699.92Z" fill="#E4751F" stroke="#E4751F" stroke-width="5.94955"/> <path d="M89.3589 912.199L137.55 866.982L169.083 980.618L89.3589 912.199Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1403.61 1699.92L1095.43 1630.31L1289.38 1529.76L1403.61 1699.92Z" fill="#233447" stroke="#233447" stroke-width="5.94955"/> <path d="M686.098 538.567L110.777 409.462L345.784 6.08252L686.098 538.567Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1631.48 2375.79L1664.2 2465.03L1134.69 2337.12L1631.48 2375.79Z" fill="#C0AD9E" stroke="#C0AD9E" stroke-width="5.94955"/> <path d="M1124.58 1861.75L1095.43 1630.31L1403.61 1699.92L1124.58 1861.75Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M826.508 1399.47L1095.43 1630.31L1124.58 1861.75L826.508 1399.47Z" fill="#E4751F" stroke="#E4751F" stroke-width="5.94955"/> <path d="M1495.83 1594.02L1731.43 1580.33L2009.87 2014.65L1495.83 1594.02ZM826.508 1399.47L1124.58 1861.75L758.088 1879.59L826.508 1399.47Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1495.83 1594.02L1788.55 2039.64L1403.61 1699.92L1495.83 1594.02Z" fill="#E4751F" stroke="#E4751F" stroke-width="5.94955"/> <path d="M1403.61 1699.92L1788.55 2039.64L1748.09 2075.93L1403.61 1699.92Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1748.09 2075.93L1124.58 1861.75L1403.61 1699.92L1748.09 2075.93ZM2009.87 2014.65L1788.55 2039.64L1495.83 1594.02L2009.87 2014.65Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M2068.18 2224.07L1972.99 2415.05L1664.2 2465.03L2068.18 2224.07ZM1664.2 2465.03L1631.48 2375.79L1710.61 2288.92L1664.2 2465.03Z" fill="#C0AD9E" stroke="#C0AD9E" stroke-width="5.94955"/> <path d="M1710.61 2288.92L1768.92 2265.72L1664.2 2465.03L1710.61 2288.92ZM1664.2 2465.03L1768.92 2265.72L2068.18 2224.07L1664.2 2465.03Z" fill="#C0AD9E" stroke="#C0AD9E" stroke-width="5.94955"/> <path d="M2009.87 2014.65L2083.05 2059.27L1860.54 2086.04L2009.87 2014.65Z" fill="#161616" stroke="#161616" stroke-width="5.94955"/> <path d="M1860.54 2086.04L1788.55 2039.64L2009.87 2014.65L1860.54 2086.04ZM1834.96 2121.15L2105.66 2088.42L2068.18 2224.07L1834.96 2121.15Z" fill="#161616" stroke="#161616" stroke-width="5.94955"/> <path d="M2068.18 2224.07L1768.92 2265.72L1834.96 2121.15L2068.18 2224.07ZM1768.92 2265.72L1710.61 2288.92L1748.09 2075.93L1768.92 2265.72ZM1748.09 2075.93L1788.55 2039.64L1860.54 2086.04L1748.09 2075.93ZM2083.05 2059.27L2105.66 2088.42L1834.96 2121.15L2083.05 2059.27Z" fill="#161616" stroke="#161616" stroke-width="5.94955"/> <path d="M1834.96 2121.15L1860.54 2086.04L2083.05 2059.27L1834.96 2121.15ZM1748.09 2075.93L1834.96 2121.15L1768.92 2265.72L1748.09 2075.93Z" fill="#161616" stroke="#161616" stroke-width="5.94955"/> <path d="M1860.54 2086.04L1834.96 2121.15L1748.09 2075.93L1860.54 2086.04Z" fill="#161616" stroke="#161616" stroke-width="5.94955"/> </g> <defs> <clipPath id="clip0_1512_1323"> <rect width="2404" height="2500" fill="white" transform="translate(0.519043 0.132812)"/> </clipPath> </defs> </svg>
									Disconnect Wallet
								  </button>
							</form>
						{% else %}
							<form id="metamask-form" method="POST" action="{% url 'home' %}" >
								{% csrf_token %}
								<button style="padding: 15px;" id='connectWallet' type="submit" class="text-gray-900 bg-white hover:bg-gray-100 border border-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-gray-600 dark:bg-gray-800 dark:border-gray-700 dark:text-white dark:hover:bg-gray-700 mr-2 mb-2">
									<svg aria-hidden="true" class="w-6 h-5 mr-2 -ml-1" viewBox="0 0 2405 2501" fill="none" xmlns="http://www.w3.org/2000/svg"> <g clip-path="url(#clip0_1512_1323)"> <path d="M2278.79 1730.86L2133.62 2221.69L1848.64 2143.76L2278.79 1730.86Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M1848.64 2143.76L2123.51 1767.15L2278.79 1730.86L1848.64 2143.76Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M2065.2 1360.79L2278.79 1730.86L2123.51 1767.15L2065.2 1360.79ZM2065.2 1360.79L2202.64 1265.6L2278.79 1730.86L2065.2 1360.79Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1890.29 1081.17L2285.34 919.338L2265.7 1007.99L1890.29 1081.17ZM2253.21 1114.48L1890.29 1081.17L2265.7 1007.99L2253.21 1114.48Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M2253.21 1114.48L2202.64 1265.6L1890.29 1081.17L2253.21 1114.48ZM2332.34 956.82L2265.7 1007.99L2285.34 919.338L2332.34 956.82ZM2253.21 1114.48L2265.7 1007.99L2318.65 1052.01L2253.21 1114.48Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1542.24 2024.17L1641 2055.7L1848.64 2143.75L1542.24 2024.17Z" fill="#E2761B" stroke="#E2761B" stroke-width="5.94955"/> <path d="M2202.64 1265.6L2253.21 1114.48L2296.64 1147.8L2202.64 1265.6ZM2202.64 1265.6L1792.71 1130.55L1890.29 1081.17L2202.64 1265.6Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1987.86 617.696L1890.29 1081.17L1792.71 1130.55L1987.86 617.696Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M2285.34 919.338L1890.29 1081.17L1987.86 617.696L2285.34 919.338Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1987.86 617.696L2400.16 570.1L2285.34 919.338L1987.86 617.696Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M2202.64 1265.6L2065.2 1360.79L1792.71 1130.55L2202.64 1265.6Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M2382.31 236.33L2400.16 570.1L1987.86 617.696L2382.31 236.33Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M2382.31 236.33L1558.3 835.45L1547.59 429.095L2382.31 236.33Z" fill="#E2761B" stroke="#E2761B" stroke-width="5.94955"/> <path d="M934.789 380.309L1547.59 429.095L1558.3 835.449L934.789 380.309Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1792.71 1130.55L1558.3 835.449L1987.86 617.696L1792.71 1130.55Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1792.71 1130.55L2065.2 1360.79L1682.65 1403.04L1792.71 1130.55Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M1682.65 1403.04L1558.3 835.449L1792.71 1130.55L1682.65 1403.04Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M1987.86 617.696L1558.3 835.45L2382.31 236.33L1987.86 617.696Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M940.144 2134.24L1134.69 2337.11L869.939 2096.16L940.144 2134.24Z" fill="#C0AD9E" stroke="#C0AD9E" stroke-width="5.94955"/> <path d="M1848.64 2143.75L1940.86 1793.33L2123.51 1767.15L1848.64 2143.75Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M151.234 1157.92L487.978 803.917L194.666 1115.67L151.234 1157.92Z" fill="#E2761B" stroke="#E2761B" stroke-width="5.94955"/> <path d="M2123.51 1767.15L1940.86 1793.33L2065.2 1360.79L2123.51 1767.15ZM1558.3 835.449L1230.48 824.74L934.789 380.309L1558.3 835.449Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M2065.2 1360.79L1940.86 1793.33L1930.74 1582.12L2065.2 1360.79Z" fill="#E4751F" stroke="#E4751F" stroke-width="5.94955"/> <path d="M1682.65 1403.04L2065.2 1360.79L1930.74 1582.12L1682.65 1403.04Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M1230.48 824.74L1558.3 835.449L1682.65 1403.04L1230.48 824.74Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1230.48 824.74L345.784 6.08252L934.79 380.309L1230.48 824.74ZM934.195 2258.58L165.513 2496.56L12.0146 1910.53L934.195 2258.58Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M265.465 1304.27L555.803 1076.41L799.14 1132.93L265.465 1304.27Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M799.139 1132.93L555.803 1076.41L686.098 538.567L799.139 1132.93Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M194.666 1115.67L555.803 1076.41L265.465 1304.27L194.666 1115.67Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1930.74 1582.12L1780.81 1506.56L1682.65 1403.04L1930.74 1582.12Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M194.666 1115.67L169.083 980.618L555.803 1076.41L194.666 1115.67Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1749.88 1676.72L1780.81 1506.56L1930.74 1582.12L1749.88 1676.72Z" fill="#233447" stroke="#233447" stroke-width="5.94955"/> <path d="M1940.86 1793.33L1749.88 1676.72L1930.74 1582.12L1940.86 1793.33Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M555.803 1076.41L169.082 980.618L137.55 866.982L555.803 1076.41ZM686.098 538.567L555.803 1076.41L137.55 866.982L686.098 538.567ZM686.098 538.567L1230.48 824.74L799.139 1132.93L686.098 538.567Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M799.14 1132.93L1230.48 824.74L1422.65 1411.96L799.14 1132.93ZM1422.65 1411.96L826.508 1399.47L799.14 1132.93L1422.65 1411.96Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M265.465 1304.27L799.14 1132.93L826.508 1399.47L265.465 1304.27ZM1682.65 1403.04L1422.65 1411.96L1230.48 824.74L1682.65 1403.04Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1780.81 1506.56L1749.88 1676.72L1682.65 1403.04L1780.81 1506.56Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M345.784 6.08252L1230.48 824.74L686.098 538.567L345.784 6.08252Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M12.0146 1910.53L758.088 1879.59L934.195 2258.58L12.0146 1910.53Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M934.194 2258.58L758.088 1879.59L1124.58 1861.75L934.194 2258.58Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M1749.88 1676.72L1940.86 1793.33L2046.16 2041.42L1749.88 1676.72ZM826.508 1399.47L12.0146 1910.53L265.465 1304.27L826.508 1399.47ZM758.088 1879.59L12.0146 1910.53L826.508 1399.47L758.088 1879.59ZM1682.65 1403.04L1731.43 1580.33L1495.83 1594.02L1682.65 1403.04ZM1495.83 1594.02L1422.65 1411.96L1682.65 1403.04L1495.83 1594.02Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1134.69 2337.11L934.194 2258.58L1631.48 2375.79L1134.69 2337.11Z" fill="#C0AD9E" stroke="#C0AD9E" stroke-width="5.94955"/> <path d="M265.465 1304.27L151.234 1157.91L194.666 1115.67L265.465 1304.27Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1710.61 2288.92L1631.48 2375.79L934.194 2258.58L1710.61 2288.92Z" fill="#D7C1B3" stroke="#D7C1B3" stroke-width="5.94955"/> <path d="M1748.09 2075.93L934.194 2258.58L1124.58 1861.75L1748.09 2075.93Z" fill="#E4761B" stroke="#E4761B" stroke-width="5.94955"/> <path d="M934.194 2258.58L1748.09 2075.93L1710.61 2288.92L934.194 2258.58Z" fill="#D7C1B3" stroke="#D7C1B3" stroke-width="5.94955"/> <path d="M137.55 866.982L110.777 409.462L686.098 538.567L137.55 866.982ZM194.665 1115.67L115.536 1035.35L169.082 980.618L194.665 1115.67Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1289.38 1529.76L1422.65 1411.96L1403.61 1699.92L1289.38 1529.76Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M1422.65 1411.96L1289.38 1529.76L1095.43 1630.31L1422.65 1411.96Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M2046.16 2041.42L2009.87 2014.65L1749.88 1676.72L2046.16 2041.42Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1095.43 1630.31L826.508 1399.47L1422.65 1411.96L1095.43 1630.31Z" fill="#CD6116" stroke="#CD6116" stroke-width="5.94955"/> <path d="M1403.61 1699.92L1422.65 1411.96L1495.83 1594.02L1403.61 1699.92Z" fill="#E4751F" stroke="#E4751F" stroke-width="5.94955"/> <path d="M89.3589 912.199L137.55 866.982L169.083 980.618L89.3589 912.199Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1403.61 1699.92L1095.43 1630.31L1289.38 1529.76L1403.61 1699.92Z" fill="#233447" stroke="#233447" stroke-width="5.94955"/> <path d="M686.098 538.567L110.777 409.462L345.784 6.08252L686.098 538.567Z" fill="#763D16" stroke="#763D16" stroke-width="5.94955"/> <path d="M1631.48 2375.79L1664.2 2465.03L1134.69 2337.12L1631.48 2375.79Z" fill="#C0AD9E" stroke="#C0AD9E" stroke-width="5.94955"/> <path d="M1124.58 1861.75L1095.43 1630.31L1403.61 1699.92L1124.58 1861.75Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M826.508 1399.47L1095.43 1630.31L1124.58 1861.75L826.508 1399.47Z" fill="#E4751F" stroke="#E4751F" stroke-width="5.94955"/> <path d="M1495.83 1594.02L1731.43 1580.33L2009.87 2014.65L1495.83 1594.02ZM826.508 1399.47L1124.58 1861.75L758.088 1879.59L826.508 1399.47Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1495.83 1594.02L1788.55 2039.64L1403.61 1699.92L1495.83 1594.02Z" fill="#E4751F" stroke="#E4751F" stroke-width="5.94955"/> <path d="M1403.61 1699.92L1788.55 2039.64L1748.09 2075.93L1403.61 1699.92Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M1748.09 2075.93L1124.58 1861.75L1403.61 1699.92L1748.09 2075.93ZM2009.87 2014.65L1788.55 2039.64L1495.83 1594.02L2009.87 2014.65Z" fill="#F6851B" stroke="#F6851B" stroke-width="5.94955"/> <path d="M2068.18 2224.07L1972.99 2415.05L1664.2 2465.03L2068.18 2224.07ZM1664.2 2465.03L1631.48 2375.79L1710.61 2288.92L1664.2 2465.03Z" fill="#C0AD9E" stroke="#C0AD9E" stroke-width="5.94955"/> <path d="M1710.61 2288.92L1768.92 2265.72L1664.2 2465.03L1710.61 2288.92ZM1664.2 2465.03L1768.92 2265.72L2068.18 2224.07L1664.2 2465.03Z" fill="#C0AD9E" stroke="#C0AD9E" stroke-width="5.94955"/> <path d="M2009.87 2014.65L2083.05 2059.27L1860.54 2086.04L2009.87 2014.65Z" fill="#161616" stroke="#161616" stroke-width="5.94955"/> <path d="M1860.54 2086.04L1788.55 2039.64L2009.87 2014.65L1860.54 2086.04ZM1834.96 2121.15L2105.66 2088.42L2068.18 2224.07L1834.96 2121.15Z" fill="#161616" stroke="#161616" stroke-width="5.94955"/> <path d="M2068.18 2224.07L1768.92 2265.72L1834.96 2121.15L2068.18 2224.07ZM1768.92 2265.72L1710.61 2288.92L1748.09 2075.93L1768.92 2265.72ZM1748.09 2075.93L1788.55 2039.64L1860.54 2086.04L1748.09 2075.93ZM2083.05 2059.27L2105.66 2088.42L1834.96 2121.15L2083.05 2059.27Z" fill="#161616" stroke="#161616" stroke-width="5.94955"/> <path d="M1834.96 2121.15L1860.54 2086.04L2083.05 2059.27L1834.96 2121.15ZM1748.09 2075.93L1834.96 2121.15L1768.92 2265.72L1748.09 2075.93Z" fill="#161616" stroke="#161616" stroke-width="5.94955"/> <path d="M1860.54 2086.04L1834.96 2121.15L1748.09 2075.93L1860.54 2086.04Z" fill="#161616" stroke="#161616" stroke-width="5.94955"/> </g> <defs> <clipPath id="clip0_1512_1323"> <rect width="2404" height="2500" fill="white" transform="translate(0.519043 0.132812)"/> </clipPath> </defs> </svg>
									Connect Wallet
								  </button>
							</form>
						{% endif %}
					</div></li>
				</ul>
				<!-- /Main navigation -->

			</div>
		</nav>
		<!-- /Nav -->

		<!-- home wrapper -->
		<div class="home-wrapper">
			<div class="container">
				<div class="row">
		
					<!-- home content -->
					<div class="col-md-10 col-md-offset-1">
						<div class="home-content">
							<div class="container">
								<div style="    display: flex;
								justify-content: center;">
									<p class="glitch">
										<span aria-hidden="true">NoCodify</span>
										NoCodify
										<span aria-hidden="true">NoCodify</span>
									  </p>
								</div>
							  </div>
							<h4>
								<p class="white-text">
									Revolutionize Your Crypto Projects with Our Powerful No-Code Development Platform – Say Goodbye to Programming and Hello to Effortless Creation!!
								</p>
							</h4>
							<div class="wallet-buttons">
								<button id='getBalance' class="white-btn" onclick="checkBalance()">Get Balance of Wallet</button>
							</div><br>
							<div class="w-full" style="    display: flex;
							align-items: center;
							justify-content: center;
							flex-direction: column;
							flex-wrap: wrap;
						">
								<div class="coding inverse-toggle px-5 pt-4 shadow-lg text-gray-100 text-sm font-mono subpixel-antialiased 
											bg-gray-800  pb-6 pt-4 rounded-lg leading-normal overflow-hidden">
									<div class="top mb-2 flex">
										<div class="h-3 w-3 bg-red-500 rounded-full"></div>
										<div class="ml-2 h-3 w-3 bg-orange-300 rounded-full"></div>
										<div class="ml-2 h-3 w-3 bg-green-500 rounded-full"></div>
									</div>
									<div class="mt-4 flex">
										{% if wallet != 'Your wallet address is the key to unlocking the magic of the blockchain. Connect it now and explore the limitless possibilities!' %}
										<span class="text-green-400">wallet:~$&nbsp;  </span>
										<p id="walletAddress"> {{ wallet.session }}<br></p>
										{% else %}
										<span class="text-green-400">computer:~$&nbsp;  </span>
										<p id="walletAddress"> {{ wallet }}<br></p>
										{% endif %}
									</div>
									<div class="mt-4 flex">
										<span class="text-green-400">Balance:~$&nbsp;</span>
										<p id="walletBalance"><span class="text-red-400">&nbsp;Permission needed</span></p>
									</div>
								</div>
							  </div>
							
						</div>
					</div>
					<!-- /home content -->
		
				</div>
			</div>
		</div>
		<!-- /home wrapper -->

	</header>
	<!-- /Header -->

	<!-- About -->
	<div id="about" class="section md-padding">

		<!-- Container -->
		<div class="container">

			<!-- Row -->
			<div class="row">

				<!-- Section header -->
				<div class="section-header text-center">
					<h2 class="title">Welcome to Our NoCodify

					</h2>
				</div>
				<!-- /Section header -->

				<!-- about -->
				<div class="XYZ">
					<div class="col-md-4">
						<div class="about">
							<i class="fa fa-cogs"></i>
							<h3>Customizable and Flexible</h3>
							<p>Our platform is fully customizable, allowing you to create a unique user experience for
								your app. Plus, our flexible architecture lets you easily integrate with other web3
								tools.</p>
						</div>
					</div>
					<!-- /about -->

					<!-- about -->
					<div class="col-md-4">
						<div class="about">
							<i class="fa fa-magic"></i>
							<h3>Explore Our Features!! </h3>
							<p>Take advantage of our awesome features, from smart contract templates to built-in
								analytics tools.</p>

						</div>
					</div>
					<!-- /about -->

					<!-- about -->
					<div class="col-md-4">
						<div class="about">
							<i class="fa fa-mobile"></i>
							<h3>Responsive and Ready </h3>
							<p>Our platform is fully responsive, ensuring that your application looks and functions
								flawlessly across all devices. </p>
						</div>
					</div>
				</div>
				<!-- /about -->

			</div>
			<!-- /Row -->

		</div>
		<!-- /Container -->

	</div>
	<!-- /About -->




	<!-- Service -->
	<div id="service" class="section md-padding">

		<!-- Container -->
		<div class="container">

			<!-- Row -->
			<div class="row">

				<!-- Section header -->
				<div class="section-header text-center">
					<h2 class="title">What we offer</h2>
				</div>
				<!-- /Section header -->
				<div class="XYZ">
					<!-- service -->
					<div class="col-md-4 col-sm-6">
						<div class="service">
							<i class="fa fa-diamond"></i>
							<h3>Build Your Decentralized App</h3>
							<p>Build decentralized applications without writing code using our user-friendly
								drag-and-drop interface. Create smart contracts, DeFi apps, NFTs, and more with ease.
							</p>
						</div>
					</div>
					<!-- /service -->

					<!-- service -->
					<div class="col-md-4 col-sm-6">
						<div class="service">
							<i class="fa fa-rocket"></i>
							<h3>Blog</h3>
							<p>Publish content and reach a wider audience with our blogging platform. Our user-friendly
								interface makes it easy to create and customize posts with no coding required.</p>
						</div>
					</div>

					<div class="col-md-4 col-sm-6">
						<div class="service">
							<i class="fa fa-cogs"></i>
							<h3>Page Creation with No Code</h3>
							<p> Build web pages without writing a single line of code. Our platform offers a
								drag-and-drop interface, making it easy for anyone to create professional-looking pages.
							</p>
						</div>
					</div>
					<!-- /service -->

					<!-- service -->
					<!-- <div class="col-md-4 col-sm-6">
						<div class="service">
							<i class="fa fa-cogs"></i>
							<h3>Auto-Generate HTML</h3>
							<p>Our auto-generating feature quickly converts your designs into HTML code, saving you time
								and effort. Whether you're a designer or developer, this tool streamlines your workflow
								and helps you create high-quality web pages effortlessly.</p>
						</div>
					</div> -->

				</div>
				<!-- /service -->
				<div class="XYZ">
					<!-- service -->
					<div class="col-md-4 col-sm-6">
						<div class="service">
							<i class="fa fa-shopping-cart"></i>
							<h3>MarketPlace</h3>
							<p> We are Offering the marketplace where you can buy and sell the nocode websites whivh are created by the users.
							</p>
						</div>
					</div>


					<!-- /service -->

					<!-- service -->
					<!-- <div class="col-md-4 col-sm-6">
						<div class="service">
							<i class="fa fa-cogs"></i>
							<h3>Compiler</h3>
							<p> Compile smart contracts with ease using our no-code compiler. Simply input your code and
								let our platform do the rest.</p>
						</div>
					</div> -->


					<!-- /service -->

					<!-- service -->
					<!-- <div class="col-md-4 col-sm-6">
						<div class="service">
							<i class="fa fa-cogs"></i>
							<h3>No-Code Automation</h3>
							<p>Automate your workflow and streamline your business processes with our no-code automation
								tools. Build custom workflows and integrations without any coding required.</p>
						</div>
					</div> -->

				</div>
				<!-- /service -->


			</div>
			<!-- /Row -->

		</div>
		<!-- /Container -->

	</div>
	<!-- /Service -->


	<!-- Why Choose Us -->



	<!-- Numbers -->


	</div>
	<!-- Row -->

	</div>
	<!-- /Container -->
	<!-- Team -->
	<div id="team" class="section ma-padding">

		<!-- Container -->
		<div class="container">

			<!-- Row -->
			<div class="row">

				<!-- Section header -->
				<div class="section-header text-center">
					<h2 class="title">Our Team</h2>
				</div>
				<!-- /Section header -->
				<div class="XYZ">
					<!-- team -->
					<div class="col-sm-4">
						<div class="team">
							<div class="team-img">
								<img class="img-responsive"
									src="https://media.licdn.com/dms/image/D5603AQFHd3kG-7zwxw/profile-displayphoto-shrink_400_400/0/1672584349709?e=1688601600&v=beta&t=J8q1KDHEBART_bf5vgtw-nKsdP0yy0-dt6eRy4odBPA"
									alt="">
								<div class="overlay">
									<div class="team-social">
										<a href="https://www.linkedin.com/in/nagi-pragalathan-n-a03a55230/"><i
												class="fa fa-linkedin"></i></a>
										<a href="https://twitter.com/NagiPragalathan"><i class="fa fa-twitter"></i></a>
										<a href="https://github.com/NagiPragalathan"><i class="fa fa-github"></i></a>
									</div>
								</div>
							</div>
							<div class="team-content">
								<h3>Nagi Pragalathan</h3>
								<span>Backend Developer</span>
							</div>
						</div>
					</div>
					<!-- /team -->

					<!-- team -->
					<div class="col-sm-4">
						<div class="team">
							<div class="team-img">
								<img class="img-responsive"
									src="https://avatars.githubusercontent.com/u/111880621?s=400&u=30361bfbe9bc8d836b3aefdd9733f8d18ec0416f&v=4"
									alt="">
								<div class="overlay">
									<div class="team-social">
										<a href="https://www.linkedin.com/in/prashant-d-7a3915249/"><i
												class="fa fa-linkedin"></i></a>
										<a href="https://twitter.com/prashantdp7"><i class="fa fa-twitter"></i></a>
										<a href="https://github.com/prashantexe"><i class="fa fa-github"></i></a>
									</div>
								</div>
							</div>
							<div class="team-content">
								<h3>D Prashant</h3>
								<span>Front-end Dev & UI/UX Designer</span>
							</div>
						</div>
					</div>
					<!-- /team -->

					<!-- team -->
					<div class="col-sm-4">
						<div class="team">
							<div class="team-img">
								<img class="img-responsive"
									src="https://media.licdn.com/dms/image/C5603AQEisaLkTowmJQ/profile-displayphoto-shrink_400_400/0/1663343489211?e=1688601600&v=beta&t=iSeDhmCUI47VDJl6b75l17O-mHt_D8q_787y2kd2Ef8"
									alt="">
								<div class="overlay">
									<div class="team-social">
										<a href="https://www.linkedin.com/in/ravindran-s-b-51b54a243/"><i
												class="fa fa-linkedin"></i></a>

										<a href="https://github.com/sbravindran03"><i class="fa fa-github"></i></a>
									</div>
								</div>
							</div>
							<div class="team-content">
								<h3>Ravidran</h3>
								<span>Front-end Developer</span>
							</div>
						</div>
					</div>
				</div>
				<!-- /team -->

				<!-- /team -->
				<!-- team -->
				<div class="col-sm-4">
					<div class="team">
						<div class="team-img">
							<img class="img-responsive"
								src="https://media.licdn.com/dms/image/D5603AQHoAy_5oYVtSg/profile-displayphoto-shrink_400_400/0/1682768627106?e=1688601600&v=beta&t=97UJ4uUGnX21A8rPjSTNUO61kk_zr0dB0XAbrODIUnE"
								alt="">
							<div class="overlay">
								<div class="team-social">
									<a href="https://www.linkedin.com/in/mani-kandan-1b0846248/"><i
											class="fa fa-linkedin"></i></a>
									<a href="https://github.com/manikandan"><i class="fa fa-github"></i></a>
								</div>
							</div>
						</div>
						<div class="team-content">
							<h3>ManiKandan</h3>
							<span>Backend developer</span>
						</div>
					</div>
				</div>


				<div class="col-sm-4">
					<div class="team">
						<div class="team-img">
							<img class="img-responsive"
								src="https://www.linkedin.com/in/karthik-s-9a6121237?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAADrtqk4B4xoK2Y_knK2wqNed3deIiPX2rBw&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3BCLZteHYgTQOUu1H1otafTA%3D%3D"
								alt="">
							<div class="overlay">
								<div class="team-social">
									<a href="https://www.linkedin.com/in/mani-kandan-1b0846248/"><i
											class="fa fa-linkedin"></i></a>
									<a href="https://github.com/manikandan"><i class="fa fa-github"></i></a>
								</div>
							</div>
						</div>
						<div class="team-content">
							<h3>S Karthik</h3>
							<span>Front-end developer</span>
						</div>
					</div>
				</div>



			</div>
			<!-- /team -->

		</div>
		<!-- /Row -->

	</div>
	<!-- /Container -->

	</div>
	<!-- /Team -->



	<!-- Contact -->
	<div id="contact" class="section md-padding">

		<!-- Container -->
		<div class="container">

			<!-- Row -->
			<div class="row">

				<!-- Section-header -->
				<div class="section-header text-center">
					<h2 class="title">Get in touch</h2>
				</div>
				<!-- /Section-header -->

				<!-- contact -->
				<div class="XYZ">
					<div class="col-sm-4">
						<div class="contact">
							<i class="fa fa-phone"></i>
							<h3>Phone</h3>
							<p>512-421-3940</p>
						</div>
					</div>
					<!-- /contact -->

					<!-- contact -->
					<div class="col-sm-4">
						<div class="contact">
							<i class="fa fa-envelope"></i>
							<h3>Email</h3>
							<p>abC@Gmail.com</p>
						</div>
					</div>
					<!-- /contact -->

					<!-- contact -->
					<div class="col-sm-4">
						<div class="contact">
							<i class="fa fa-map-marker"></i>
							<h3>Address</h3>
							<p>Chennai, Tamil Nadu</p>
						</div>
					</div>
				</div>
				<!-- /contact -->

				<!-- contact form -->
				<div class="col-md-8 col-md-offset-2">
					<form class="contact-form">
						<input type="text" class="input" placeholder="Name">
						<input type="email" class="input" placeholder="Email">
						<input type="text" class="input" placeholder="Subject">
						<textarea class="input" placeholder="Message"></textarea>
						<button class="main-btn">Send message</button>
					</form>
				</div>
				<!-- /contact form -->

			</div>
			<!-- /Row -->

		</div>
		<!-- /Container -->

	</div>
	<!-- /Contact -->
	<!-- CHAT BAR BLOCK -->
    <div class="chat-bar-collapsible" style="    z-index: 99;	">
        <button id="chat-button" type="button" class="collapsible">Chat with us!
            <i id="chat-icon" style="color: #fff;" class="fa fa-fw fa-comments-o"></i>
        </button>

        <div class="content">
            <div class="full-chat-block">
                <!-- Message Container -->
                <div class="outer-container">
                    <div class="chat-container">
                        <!-- Messages -->
                        <div id="chatbox">
                            <h5 id="chat-timestamp"></h5>
                            <p id="botStarterMessage" class="botText"><span>Loading...</span></p>
                        </div>

                        <!-- User input box -->
                        <div class="chat-bar-input-block">
                            <div id="userInput">
                                <input id="textInput" class="input-box" type="text" name="msg"
                                    placeholder="Tap 'Enter' to send a message">
                                <p></p>
                            </div>

                            <div class="chat-bar-icons">
                                <i id="chat-icon" style="color: crimson;" class="fa fa-fw fa-heart"
                                    onclick="heartButton()"></i>
                                <i id="chat-icon" style="color: #333;" class="fa fa-fw fa-send"
                                    onclick="sendButton()"></i>
                            </div>
                        </div>

                        <div id="chat-bar-bottom">
                            <p></p>
                        </div>

                    </div>
                </div>

            </div>
        </div>

    </div>

	<!-- Footer -->
	<footer id="footer" class="sm-padding bg-dark">

		<!-- Container -->
		<div class="container">

			<!-- Row -->
			<div class="row">

				<div class="col-md-12">

					<!-- footer logo -->
					<div class="footer-logo">
						<a href=" {% static 'index.html' %} "><img src=" {% static 'img/logo-alt.png' %} "
								alt="logo"></a>
					</div>
					<!-- /footer logo -->

					<!-- footer follow -->
					<ul class="footer-follow">
						<li><a href="https://twitter.com/NagiPragalathan"><i class="fa fa-twitter"></i></a></li>
						<li><a href="https://github.com/NagiPragalathan"><i class="fa fa-github"></i></a></li>
						<li><a href="https://www.linkedin.com/in/nagi-pragalathan-n-a03a55230/"><i
									class="fa fa-linkedin"></i></a></li>
						<li><a href="https://www.youtube.com/@gryffindorsguild"><i class="fa fa-youtube"></i></a></li>
					</ul>
					<!-- /footer follow -->

					<!-- footer copyright -->
					<div class="footer-copyright">
						<p>Copyright © 2023. All Rights Reserved. </p>
					</div>
					<!-- /footer copyright -->

				</div>

			</div>
			<!-- /Row -->

		</div>
		<!-- /Container -->

	</footer>
	<!-- /Footer -->

	<!-- Back to top -->
	<div id="back-to-top"></div>
	<!-- /Back to top -->

	<!-- Preloader -->
	<div id="preloader">
		<div class="preloader">
			<span></span>
			<span></span>
			<span></span>
			<span></span>
		</div>
	</div>
	<!-- /Preloader -->

	<!-- jQuery Plugins -->
	<script src="https://cdn.jsdelivr.net/npm/web3@1.4.0/dist/web3.min.js"></script>

	<script type="text/javascript" src=" {% static 'js/jquery.min.js' %} "></script>
	<script type="text/javascript" src=" {% static 'js/bootstrap.min.js' %} "></script>
	<script type="text/javascript" src=" {% static 'js/owl.carousel.min.js' %} "></script>
	<script type="text/javascript" src=" {% static 'js/jquery.magnific-popup.js' %} "></script>
	<script type="text/javascript" src=" {% static 'js/main.js' %} "></script>
	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
    <script src="https://code.iconify.design/iconify-icon/1.0.3/iconify-icon.min.js"></script>


	<script>
		window.userWalletAddress = null
      const connectWallet = document.getElementById('connectWallet')
      const walletAddress = document.getElementById('walletAddress')
      const walletBalance = document.getElementById('walletBalance')



      function checkInstalled() {
        if (typeof window.ethereum == 'undefined') {
          connectWallet.innerText = 'MetaMask isnt installed, please install it'
          connectWallet.classList.remove()
          connectWallet.classList.add()
          return false
        }
        connectWallet.addEventListener('click', connectWalletwithMetaMask)
      }

      async function connectWalletwithMetaMask() {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' })
        .catch((e) => {
        console.error(e.message)
        return
        })

        if (!accounts) { return }

          window.userWalletAddress = accounts[0]
          Send_Data("save_wallet_address",window.userWalletAddress)
          walletAddress.innerText = window.userWalletAddress

          connectWallet.innerText = 'Disconnect Wallet'
          connectWallet.removeEventListener('click', connectWalletwithMetaMask)
          setTimeout(() => {
            connectWallet.addEventListener('click', signOutOfMetaMask)
          }, 200)
      }


      function signOutOfMetaMask() {
        window.userwalletAddress = null
        walletAddress.innerText = 'Your wallet address is the key to unlocking the magic of the blockchain. Connect it now and explore the limitless possibilities!'
        connectWallet.innerText = 'Connect Wallet'

        connectWallet.removeEventListener('click', signOutOfMetaMask)
        setTimeout(() => {
          connectWallet.addEventListener('click', connectWalletwithMetaMask)
        }, 200  )
      }

      async function checkBalance() {
        let balance = await window.ethereum.request({ 
			method: "eth_getBalance",
			params: [
			  `{{ wallet.session }}`,
			  'latest'
			]
		  }).catch((err)=> {
			  console.log(err)
		  })

      console.log(parseFloat((balance) / Math.pow(10,18)))

      walletBalance.innerText = parseFloat((balance) / Math.pow(10,18))
    }

      window.addEventListener('DOMContentLoaded', () => {
        checkInstalled()
      })



      function Send_Data(url,data) {

        $.ajax({
            method: "POST",
            url: url,
            data: {
              "csrfmiddlewaretoken":$("input[name=csrfmiddlewaretoken]").val(),
              'wallet_address':data,
            },
            success: function (data) {
                location.reload();
            }
        });
}

	</script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
	<script>
		// Collapsible
var coll = document.getElementsByClassName("collapsible");

for (let i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        this.classList.toggle("active");

        var content = this.nextElementSibling;

        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }

    });
}

function getTime() {
    let today = new Date();
    hours = today.getHours();
    minutes = today.getMinutes();

    if (hours < 10) {
        hours = "0" + hours;
    }

    if (minutes < 10) {
        minutes = "0" + minutes;
    }

    let time = hours + ":" + minutes;
    return time;
}

// Gets the first message
function firstBotMessage() {
    let firstMessage = "How's it going?"
    document.getElementById("botStarterMessage").innerHTML = '<p class="botText"><span>' + firstMessage + '</span></p>';

    let time = getTime();

    $("#chat-timestamp").append(time);
    document.getElementById("userInput").scrollIntoView(false);
}

firstBotMessage();

// Retrieves the response
function getHardResponse(userText) {
    let botResponse = getBotResponse(userText);
    let botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
    $("#chatbox").append(botHtml);

    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

//Gets the text text from the input box and processes it
function getResponse() {
    let userText = $("#textInput").val();

    if (userText == "") {
        userText = "I love Code Palace!";
    }

    let userHtml = '<p class="userText"><span>' + userText + '</span></p>';

    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);

    setTimeout(() => {
        getHardResponse(userText);
    }, 1000)

}

// Handles sending text via button clicks
function buttonSendText(sampleText) {
    let userHtml = '<p class="userText"><span>' + sampleText + '</span></p>';

    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);

    //Uncomment this if you want the bot to respond to this buttonSendText event
    // setTimeout(() => {
    //     getHardResponse(sampleText);
    // }, 1000)
}

function sendButton() {
    getResponse();
}

function heartButton() {
    buttonSendText("Heart clicked!")
}

// Press enter to send a message
$("#textInput").keypress(function (e) {
    if (e.which == 13) {
        getResponse();
    }
});
function getBotResponse(input) {
    //rock paper scissors
    if (input == "rock") {
        return "paper";
    } else if (input == "paper") {
        return "scissors";
    } else if (input == "scissors") {
        return "rock";
    }

    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else {
        return "Try asking something else!";
    }
}
	</script>
	
</body>

</html>
