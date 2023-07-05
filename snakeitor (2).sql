-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-06-2023 a las 21:36:03
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `snakeitor`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `precio` int(11) NOT NULL,
  `stock` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `nombre`, `precio`, `stock`) VALUES
(15, 'Papitas fritas sabor queso', 1000, 100),
(16, 'Refresco de cola', 500, 188),
(17, 'Barra de chocolate con almendras', 800, 147),
(18, 'Paquete de galletas de avena', 300, 80),
(19, 'Agua mineral sin gas', 600, 116),
(20, 'Mix de frutos secos', 1200, 90),
(21, 'Barra de cereal energética', 700, 180),
(23, 'Paquete de chicles surtidos', 1500, 140),
(24, 'Bebida isotónica de limón', 400, 148),
(25, 'Mani', 400, 0),
(27, 'elmejorsnack', 800, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `id` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL,
  `fecha_venta` timestamp NOT NULL DEFAULT current_timestamp(),
  `cantidad` int(11) NOT NULL,
  `total` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`id`, `producto_id`, `fecha_venta`, `cantidad`, `total`) VALUES
(22, 24, '2023-06-26 03:35:02', 10, 4000),
(23, 16, '2023-06-26 03:35:56', 2, 1000),
(24, 19, '2023-06-26 03:36:07', 2, 1200),
(25, 17, '2023-06-26 03:46:07', 3, 2400),
(26, 25, '2023-06-26 03:48:54', 3, 1200),
(27, 25, '2023-06-26 03:51:52', 11, 4400),
(28, 25, '2023-06-26 03:52:12', 6, 2400),
(29, 19, '2023-06-29 22:40:47', 2, 1200),
(30, 16, '2023-06-30 16:58:06', 2, 1000),
(31, 16, '2023-06-30 16:59:34', 2, 1000),
(32, 16, '2023-06-30 17:00:36', 2, 1000),
(33, 16, '2023-06-30 17:01:18', 2, 1000),
(34, 16, '2023-06-30 17:24:49', 2, 1000),
(35, 24, '2023-06-30 17:38:16', 2, 800);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `producto_id` (`producto_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`producto_id`) REFERENCES `productos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
