-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-07-2023 a las 13:45:26
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cinelandia`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargo`
--

CREATE TABLE `cargo` (
  `id_cargo` int(11) NOT NULL,
  `descripcion_cargo` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `cargo`
--

INSERT INTO `cargo` (`id_cargo`, `descripcion_cargo`) VALUES
(1, 'administrador'),
(2, 'empleado'),
(3, 'caja');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id_categoria` int(11) NOT NULL,
  `descripcion_categoria` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_usuario`
--

CREATE TABLE `datos_usuario` (
  `ci_usuario` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `telefono` bigint(20) NOT NULL,
  `id_prefijo_cedula` int(11) NOT NULL,
  `id_prefijo_celular` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `datos_usuario`
--

INSERT INTO `datos_usuario` (`ci_usuario`, `nombre`, `apellido`, `direccion`, `telefono`, `id_prefijo_cedula`, `id_prefijo_celular`) VALUES
(2766, 'katalina', 'ormaza', 'bdckjdsbsdkuhsd', 4247108059, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `id_prefijo_cedula`
--

CREATE TABLE `id_prefijo_cedula` (
  `id_prefijo_cedula` int(11) NOT NULL,
  `descripcion_prefijo_cedula` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `id_prefijo_cedula`
--

INSERT INTO `id_prefijo_cedula` (`id_prefijo_cedula`, `descripcion_prefijo_cedula`) VALUES
(1, 'V-'),
(2, 'E-'),
(3, 'P-'),
(4, 'J-');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `id_prefijo_celular`
--

CREATE TABLE `id_prefijo_celular` (
  `id_prefijo_celular` int(11) NOT NULL,
  `descripcion_prefijo_celular` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `id_prefijo_celular`
--

INSERT INTO `id_prefijo_celular` (`id_prefijo_celular`, `descripcion_prefijo_celular`) VALUES
(1, '+58'),
(2, '+57');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `ci_usuario` int(11) NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `contraseña` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `id_cargo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `ci_usuario`, `usuario`, `contraseña`, `correo`, `fecha_ingreso`, `id_cargo`) VALUES
(2, 2766, 'katalina', '123456', 'jkhshsuysksn', '2023-12-12', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cargo`
--
ALTER TABLE `cargo`
  ADD PRIMARY KEY (`id_cargo`);

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id_categoria`);

--
-- Indices de la tabla `datos_usuario`
--
ALTER TABLE `datos_usuario`
  ADD PRIMARY KEY (`ci_usuario`),
  ADD KEY `id_prefijo_celular` (`id_prefijo_cedula`),
  ADD KEY `datos_usuario_ibfk_1` (`id_prefijo_celular`);

--
-- Indices de la tabla `id_prefijo_cedula`
--
ALTER TABLE `id_prefijo_cedula`
  ADD PRIMARY KEY (`id_prefijo_cedula`);

--
-- Indices de la tabla `id_prefijo_celular`
--
ALTER TABLE `id_prefijo_celular`
  ADD PRIMARY KEY (`id_prefijo_celular`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `ci_usuario` (`ci_usuario`),
  ADD KEY `id_cargo` (`id_cargo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cargo`
--
ALTER TABLE `cargo`
  MODIFY `id_cargo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `id_prefijo_cedula`
--
ALTER TABLE `id_prefijo_cedula`
  MODIFY `id_prefijo_cedula` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `id_prefijo_celular`
--
ALTER TABLE `id_prefijo_celular`
  MODIFY `id_prefijo_celular` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `datos_usuario`
--
ALTER TABLE `datos_usuario`
  ADD CONSTRAINT `datos_usuario_ibfk_1` FOREIGN KEY (`id_prefijo_celular`) REFERENCES `id_prefijo_celular` (`id_prefijo_celular`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `datos_usuario_ibfk_2` FOREIGN KEY (`id_prefijo_cedula`) REFERENCES `id_prefijo_cedula` (`id_prefijo_cedula`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`id_cargo`) REFERENCES `cargo` (`id_cargo`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `usuario_ibfk_2` FOREIGN KEY (`ci_usuario`) REFERENCES `datos_usuario` (`ci_usuario`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
