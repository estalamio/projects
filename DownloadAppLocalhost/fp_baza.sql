-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 16, 2020 at 12:59 AM
-- Server version: 8.0.18
-- PHP Version: 5.6.39

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fp_baza`
--

-- --------------------------------------------------------

--
-- Table structure for table `informacije`
--

CREATE TABLE `informacije` (
  `id` int(11) NOT NULL,
  `imeFajla` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `datum` varchar(150) NOT NULL,
  `vreme` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `informacije`
--

INSERT INTO `informacije` (`id`, `imeFajla`, `datum`, `vreme`) VALUES
(170, 'Vezba6.sql', '2020-06-05 12:30:30.806886', '12:30:30');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `informacije`
--
ALTER TABLE `informacije`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `informacije`
--
ALTER TABLE `informacije`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=171;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
