-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-10-2023 a las 00:48:50
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
(2, 'empleado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id_categoria` int(11) NOT NULL,
  `descripcion_categoria` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`id_categoria`, `descripcion_categoria`) VALUES
(1, 'chocolates'),
(2, 'pepitos');

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
  `id_prefijo_documento` int(11) NOT NULL,
  `id_prefijo_celular` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `datos_usuario`
--

INSERT INTO `datos_usuario` (`ci_usuario`, `nombre`, `apellido`, `direccion`, `telefono`, `id_prefijo_documento`, `id_prefijo_celular`) VALUES
(2766, 'katalina', 'ormaza', 'bdckjdsbsdkuhsd', 4247108059, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalles_movimientos`
--

CREATE TABLE `detalles_movimientos` (
  `id_detalles` int(11) NOT NULL,
  `id_movimientos` int(11) NOT NULL,
  `id_productos` int(11) NOT NULL,
  `precio_unitario` decimal(4,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movimientos`
--

CREATE TABLE `movimientos` (
  `id_movimientos` int(11) NOT NULL,
  `descripcion_movimiento` varchar(60) NOT NULL,
  `id_status_movimientos` int(11) NOT NULL,
  `total` decimal(6,2) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `fecha_registro` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `movimientos`
--

INSERT INTO `movimientos` (`id_movimientos`, `descripcion_movimiento`, `id_status_movimientos`, `total`, `id_usuario`, `fecha_registro`) VALUES
(17, '10', 2, '40.00', 13, '2023-10-22'),
(18, '10', 2, '10.00', 13, '2023-10-22'),
(19, '21', 1, '1.00', 12, '2023-10-23');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prefijo_celular`
--

CREATE TABLE `prefijo_celular` (
  `id_prefijo_celular` int(11) NOT NULL,
  `descripcion_prefijo_celular` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `prefijo_celular`
--

INSERT INTO `prefijo_celular` (`id_prefijo_celular`, `descripcion_prefijo_celular`) VALUES
(1, '+58'),
(2, '+57');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prefijo_documento`
--

CREATE TABLE `prefijo_documento` (
  `id_prefijo_cedula` int(11) NOT NULL,
  `descripcion_prefijo_cedula` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `prefijo_documento`
--

INSERT INTO `prefijo_documento` (`id_prefijo_cedula`, `descripcion_prefijo_cedula`) VALUES
(1, 'V-'),
(2, 'E-'),
(3, 'P-'),
(4, 'J-');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id_producto` int(11) NOT NULL,
  `descripcion_producto` varchar(60) NOT NULL,
  `cantidad_total` int(11) NOT NULL,
  `fecha_vencimiento` date NOT NULL,
  `id_proveedor` int(11) NOT NULL,
  `id_categoria` int(11) NOT NULL,
  `precio_unitario` decimal(4,2) NOT NULL,
  `costo_mayor` decimal(6,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id_producto`, `descripcion_producto`, `cantidad_total`, `fecha_vencimiento`, `id_proveedor`, `id_categoria`, `precio_unitario`, `costo_mayor`) VALUES
(1, 'cri cri', 12, '2024-07-25', 1, 1, '1.50', '15.00'),
(2, 'doritos', 12, '2024-07-25', 2, 2, '4.00', '18.00'),
(7, 'helados', 3, '2023-12-12', 2, 2, '2.00', '50.00'),
(10, 'pepitos', 10, '2025-12-12', 3, 2, '12.00', '5.00'),
(21, 'helado chocolate', 0, '2024-12-12', 1, 2, '10.00', '2.00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE `proveedor` (
  `id_proveedor` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `codigo` int(11) NOT NULL,
  `id_prefijo_documento` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `proveedor`
--

INSERT INTO `proveedor` (`id_proveedor`, `nombre`, `codigo`, `id_prefijo_documento`) VALUES
(1, 'Nestle', 1234, 1),
(2, 'Jacks', 2345, 1),
(3, 'pepito', 123456, 2),
(4, '1', 123, 1),
(5, 'trululu', 434566, 1),
(6, 'polar', 123333, 1),
(8, 'efe', 1222333444, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `status_movimientos`
--

CREATE TABLE `status_movimientos` (
  `id_status_movimientos` int(11) NOT NULL,
  `descripcion_status` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `status_movimientos`
--

INSERT INTO `status_movimientos` (`id_status_movimientos`, `descripcion_status`) VALUES
(1, 'Venta'),
(2, 'Compra');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `ci_usuario` int(11) NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `contraseña` varchar(50) NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `id_cargo` int(11) NOT NULL,
  `ci_prefijo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `ci_usuario`, `usuario`, `contraseña`, `fecha_ingreso`, `id_cargo`, `ci_prefijo`) VALUES
(2, 2766, 'katalina', '123456', '2023-12-12', 1, 0),
(12, 123456, 'usuario', '123', '0000-00-00', 2, 0),
(13, 12345, 'admin', '123', '0000-00-00', 1, 0),
(14, 1222, 'sistema', '123', '2023-09-27', 1, 0),
(15, 1222, 'cine', '123', '2023-09-28', 1, 0),
(16, 239872398, 'cinelandia', '123', '2023-09-28', 1, 0),
(17, 123, 'asdsadasd', '123', '2023-10-08', 1, 0);

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
  ADD KEY `id_prefijo_celular` (`id_prefijo_documento`),
  ADD KEY `datos_usuario_ibfk_1` (`id_prefijo_celular`);

--
-- Indices de la tabla `detalles_movimientos`
--
ALTER TABLE `detalles_movimientos`
  ADD PRIMARY KEY (`id_detalles`),
  ADD KEY `id_productos` (`id_productos`),
  ADD KEY `id_movimientos` (`id_movimientos`);

--
-- Indices de la tabla `movimientos`
--
ALTER TABLE `movimientos`
  ADD PRIMARY KEY (`id_movimientos`),
  ADD KEY `id_status_movimientos` (`id_status_movimientos`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `prefijo_celular`
--
ALTER TABLE `prefijo_celular`
  ADD PRIMARY KEY (`id_prefijo_celular`);

--
-- Indices de la tabla `prefijo_documento`
--
ALTER TABLE `prefijo_documento`
  ADD PRIMARY KEY (`id_prefijo_cedula`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id_producto`),
  ADD KEY `id_proveedor` (`id_proveedor`),
  ADD KEY `id_categoria` (`id_categoria`);

--
-- Indices de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD PRIMARY KEY (`id_proveedor`),
  ADD KEY `id_prefijo_documento` (`id_prefijo_documento`);

--
-- Indices de la tabla `status_movimientos`
--
ALTER TABLE `status_movimientos`
  ADD PRIMARY KEY (`id_status_movimientos`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `ci_usuario` (`ci_usuario`),
  ADD KEY `id_cargo` (`id_cargo`),
  ADD KEY `ci_prefijo` (`ci_prefijo`);

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
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `detalles_movimientos`
--
ALTER TABLE `detalles_movimientos`
  MODIFY `id_detalles` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `movimientos`
--
ALTER TABLE `movimientos`
  MODIFY `id_movimientos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `prefijo_celular`
--
ALTER TABLE `prefijo_celular`
  MODIFY `id_prefijo_celular` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `prefijo_documento`
--
ALTER TABLE `prefijo_documento`
  MODIFY `id_prefijo_cedula` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  MODIFY `id_proveedor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `status_movimientos`
--
ALTER TABLE `status_movimientos`
  MODIFY `id_status_movimientos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `datos_usuario`
--
ALTER TABLE `datos_usuario`
  ADD CONSTRAINT `datos_usuario_ibfk_1` FOREIGN KEY (`id_prefijo_celular`) REFERENCES `prefijo_celular` (`id_prefijo_celular`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `datos_usuario_ibfk_2` FOREIGN KEY (`id_prefijo_documento`) REFERENCES `prefijo_documento` (`id_prefijo_cedula`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `detalles_movimientos`
--
ALTER TABLE `detalles_movimientos`
  ADD CONSTRAINT `detalles_movimientos_ibfk_1` FOREIGN KEY (`id_movimientos`) REFERENCES `movimientos` (`id_movimientos`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `detalles_movimientos_ibfk_2` FOREIGN KEY (`id_productos`) REFERENCES `productos` (`id_producto`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `movimientos`
--
ALTER TABLE `movimientos`
  ADD CONSTRAINT `movimientos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `movimientos_ibfk_2` FOREIGN KEY (`id_status_movimientos`) REFERENCES `status_movimientos` (`id_status_movimientos`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedor` (`id_proveedor`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `productos_ibfk_2` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id_categoria`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD CONSTRAINT `proveedor_ibfk_1` FOREIGN KEY (`id_prefijo_documento`) REFERENCES `prefijo_documento` (`id_prefijo_cedula`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`id_cargo`) REFERENCES `cargo` (`id_cargo`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
