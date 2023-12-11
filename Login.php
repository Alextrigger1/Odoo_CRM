<?php
	$con = mysqli_connect("localhost", "root", "", "usuarios");
	
	
	$correo = $_POST["correo"];
	$contraseña = $_POST["contraseña"];
	
	$statement = mysqli_prepare($con, "SELECT * FROM user WHERE correo = ? AND contraseña = ?");

	mysqli_stmt_bind_param($statement, "ss", $correo, $contraseña);
	mysqli_stmt_execute($statement);

	mysqli_stmt_store_result($statement);
	mysqli_stmt_bind_result($statement, $userID, $nombre, $correo, $contraseña, $direccion, $telefono);

	$response = array();
	$response["success"] = false;

	while(mysqli_stmt_fetch($statement)){
		$response["success"] = true;
		$response["nombre"] = $nombre;
		$response["correo"] = $correo;
		$response["contraseña"] = $contraseña;
		$response["direccion"] = $direccion;
		$response["telefono"] = $telefono;
	}



	echo json_encode($response);
?>

