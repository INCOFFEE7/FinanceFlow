-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 09, 2021 at 07:10 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `finance_flow`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `transaksi_keluar` (IN `tujuan_pengeluaran` VARCHAR(50), IN `jumlah_uang_keluar` INT, IN `keterangan_uang_keluar` VARCHAR(100))  NO SQL
BEGIN
	INSERT INTO transaksi (keterangan_transaksi,total_transaksi, total_uang) VALUES(tujuan_pengeluaran,jumlah_uang_keluar, -jumlah_uang_keluar);
	INSERT INTO transaksi_keluar(id_transaksi,keterangan_keluar,waktu_keluar,jumlah_keluar,keterangan_keluar_tambahan) 
	VALUES (LAST_INSERT_ID(),tujuan_pengeluaran,NOW(),jumlah_uang_keluar,keterangan_uang_keluar);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `transaksi_masuk` (IN `asal_pemasukkan` VARCHAR(50), IN `jumlah_uang_masuk` INT, IN `keterangan_uang_masuk` VARCHAR(100))  NO SQL
BEGIN
	INSERT INTO transaksi(keterangan_transaksi,total_transaksi,total_uang) 	 VALUES(asal_pemasukkan,jumlah_uang_masuk,jumlah_uang_masuk);
	INSERT INTO transaksi_masuk(id_transaksi,keterangan_masuk,waktu_masuk,jumlah_masuk,keterangan_masuk_tambahan) 
	VALUES (LAST_INSERT_ID(),asal_pemasukkan,NOW(),jumlah_uang_masuk,keterangan_uang_masuk);
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `id_transaksi` int(11) NOT NULL,
  `keterangan_transaksi` varchar(50) NOT NULL,
  `total_transaksi` int(25) NOT NULL,
  `last_update` datetime NOT NULL DEFAULT current_timestamp(),
  `total_uang` int(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transaksi_keluar`
--

CREATE TABLE `transaksi_keluar` (
  `id_transaksi_keluar` int(11) NOT NULL,
  `id_transaksi` int(11) NOT NULL,
  `keterangan_keluar` varchar(50) NOT NULL,
  `jumlah_keluar` int(25) NOT NULL,
  `waktu_keluar` datetime NOT NULL DEFAULT current_timestamp(),
  `keterangan_keluar_tambahan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transaksi_masuk`
--

CREATE TABLE `transaksi_masuk` (
  `id_transaksi_masuk` int(11) NOT NULL,
  `id_transaksi` int(11) NOT NULL,
  `keterangan_masuk` varchar(50) NOT NULL,
  `jumlah_masuk` int(25) NOT NULL,
  `waktu_masuk` datetime NOT NULL DEFAULT current_timestamp(),
  `keterangan_masuk_tambahan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id_transaksi`);

--
-- Indexes for table `transaksi_keluar`
--
ALTER TABLE `transaksi_keluar`
  ADD PRIMARY KEY (`id_transaksi_keluar`),
  ADD KEY `id_transaksi_keluar` (`id_transaksi`);

--
-- Indexes for table `transaksi_masuk`
--
ALTER TABLE `transaksi_masuk`
  ADD PRIMARY KEY (`id_transaksi_masuk`),
  ADD KEY `id_transaksi_masuk` (`id_transaksi`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `id_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `transaksi_keluar`
--
ALTER TABLE `transaksi_keluar`
  MODIFY `id_transaksi_keluar` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `transaksi_masuk`
--
ALTER TABLE `transaksi_masuk`
  MODIFY `id_transaksi_masuk` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `transaksi_keluar`
--
ALTER TABLE `transaksi_keluar`
  ADD CONSTRAINT `id_transaksi_keluar` FOREIGN KEY (`id_transaksi`) REFERENCES `transaksi` (`id_transaksi`) ON DELETE CASCADE;

--
-- Constraints for table `transaksi_masuk`
--
ALTER TABLE `transaksi_masuk`
  ADD CONSTRAINT `id_transaksi_masuk` FOREIGN KEY (`id_transaksi`) REFERENCES `transaksi` (`id_transaksi`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
