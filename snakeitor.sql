-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-07-2023 a las 03:25:43
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
(15, 'Papitas fritas sabor queso', 1000, 41),
(16, 'Refresco de cola', 500, 175),
(17, 'Barra de chocolate con almendras', 800, 146),
(18, 'Paquete de galletas de avena', 300, 0),
(19, 'Agua mineral sin gas', 600, 116),
(20, 'Mix de frutos secos', 1200, 88),
(21, 'Barra de cereal energética', 700, 180),
(23, 'Paquete de chicles surtidos', 1500, 0),
(24, 'Bebida isotónica de limón', 400, 147),
(25, 'Mani', 400, 0),
(27, 'elmejorsnack', 800, 0),
(28, 'klg', 300, 0),
(29, 'asdf', 100, 0),
(30, 'lsls2', 200, -7),
(31, 'asdasd', 100, 0),
(32, 'asdfasdasda', 2, -1),
(33, 'uni', 100, 0),
(34, 'lol', 100, 0),
(35, 'tyu', 100, 0),
(36, 'opl', 100, 0),
(37, 'ops', 100, 0),
(38, 'ops2', 100, 0),
(39, 'okl', 100, -21),
(40, 'okl2', 200, 0),
(41, 'okl3', 100, -18),
(42, 'opsss', 100, 0),
(43, 'asdasd', 100, 0),
(44, 'asdsadasdsadsadasdadasd', 100, 0),
(45, 'asdsadasd', 100, -8),
(46, 'sadasdad', 299, 0),
(47, 'asdsadsadsdadsdadd', 100, 0),
(48, 'asdsadadasdadsdasdsad', 100, 0),
(49, 'adasdds', 10, 0),
(50, 'asdsadasdasdadsadadasdsdasdad', 100, 0),
(51, 'los2', 200, 0),
(52, 'los3', 2, 0),
(53, 'los4', 100, 0),
(54, 'asdasdasd', 200, 0),
(55, 'adssadads', 20, 0),
(56, 'asdasdsdadasd', 200, 2),
(57, 'asdasdsdadasd', 200, 2),
(58, 'asdasdsdadasd', 200, 2),
(59, 'asdasdsdadasd', 200, 2),
(60, 'asdasdsdadasd', 200, 2),
(61, 'ewqeq', 3, 3),
(62, 'los22', 100, 2),
(63, 'dasddasdad', 10, 10),
(64, 'therequiem', 900, 10),
(65, 'matisinmanos', 1, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL COMMENT 'Primary Key',
  `user` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `user`, `password`) VALUES
(3, 'miguel', 'pbkdf2:sha256:600000$diBMShw3M3VhncLV$cadc6d831924840eac92ec2ff94e74d356cbfa38b527724e78b97f7b374b8a0d'),
(4, 'leodan', 'pbkdf2:sha256:600000$AxjDytb70Sde2MSw$a61ba37d0ee0a8feb7baf7d1f703e60c16e9416b433621aed8f22da5cbcc1246');

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
(133, 15, '2023-07-05 04:20:24', 1, 1000),
(134, 15, '2023-07-05 04:20:26', 1, 1000),
(135, 15, '2023-07-05 04:20:28', 1, 1000),
(136, 15, '2023-07-05 04:20:54', 1, 1000),
(137, 15, '2023-07-05 04:21:02', 1, 1000),
(138, 15, '2023-07-05 04:21:35', 1, 1000),
(139, 16, '2023-07-05 04:21:41', 1, 500),
(140, 15, '2023-07-05 04:22:41', 1, 1000),
(141, 15, '2023-07-05 04:22:47', 1, 1000),
(142, 15, '2023-07-05 04:24:24', 1, 1000),
(143, 15, '2023-07-05 04:24:33', 1, 1000),
(144, 15, '2023-07-05 04:24:35', 1, 1000),
(145, 15, '2023-07-05 04:24:37', 1, 1000),
(146, 15, '2023-07-05 04:24:39', 1, 1000),
(147, 15, '2023-07-05 04:25:14', 10, 10000),
(148, 15, '2023-07-05 04:25:23', 10, 10000),
(149, 15, '2023-07-05 04:28:59', 1, 1000),
(150, 15, '2023-07-05 04:29:02', 1, 1000),
(151, 15, '2023-07-05 04:29:03', 1, 1000),
(152, 15, '2023-07-05 04:29:04', 1, 1000),
(153, 15, '2023-07-05 04:29:14', 1, 1000),
(154, 15, '2023-07-05 04:30:47', 20, 20000),
(155, 15, '2023-07-05 04:30:57', 1, 1000),
(156, 15, '2023-07-05 04:33:19', 1, 1000),
(157, 15, '2023-07-05 04:33:23', 1, 1000),
(158, 15, '2023-07-05 04:33:26', 1, 1000),
(159, 15, '2023-07-05 04:33:30', 1, 1000),
(160, 15, '2023-07-05 04:33:32', 1, 1000),
(161, 15, '2023-07-05 04:45:41', 1, 1000),
(162, 15, '2023-07-05 04:45:44', 1, 1000),
(163, 15, '2023-07-05 04:45:47', 1, 1000),
(164, 15, '2023-07-05 04:45:51', 1, 1000),
(165, 15, '2023-07-05 04:50:44', 1, 1000),
(166, 15, '2023-07-05 04:50:46', 1, 1000),
(167, 15, '2023-07-05 04:50:47', 1, 1000),
(168, 15, '2023-07-05 04:50:49', 1, 1000),
(169, 16, '2023-07-05 04:51:23', 2, 1000),
(170, 16, '2023-07-05 04:51:24', 2, 1000),
(171, 16, '2023-07-05 04:51:26', 2, 1000),
(172, 16, '2023-07-05 04:51:27', 2, 1000),
(173, 15, '2023-07-05 04:51:29', 1, 1000),
(174, 15, '2023-07-05 04:51:30', 1, 1000),
(175, 15, '2023-07-05 04:53:47', 1, 1000),
(176, 15, '2023-07-05 04:53:50', 1, 1000),
(177, 15, '2023-07-05 05:09:36', 1, 1000),
(178, 15, '2023-07-05 05:10:03', 1, 1000),
(179, 15, '2023-07-05 05:10:05', 1, 1000),
(180, 15, '2023-07-14 07:22:04', 2, 2000),
(181, 15, '2023-07-14 07:22:28', 2, 2000),
(182, 65, '2023-07-18 22:11:53', 10, 10);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary Key', AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=183;

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
