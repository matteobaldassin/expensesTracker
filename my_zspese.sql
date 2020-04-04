-- phpMyAdmin SQL Dump
-- version 4.1.7
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 04, 2020 alle 18:31
-- Versione del server: 5.6.33-log
-- PHP Version: 5.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `my_zspese`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `categorie`
--

CREATE TABLE IF NOT EXISTS `categorie` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(32) NOT NULL,
  `coloreRiga` varchar(32) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dump dei dati per la tabella `categorie`
--

INSERT INTO `categorie` (`ID`, `nome`, `coloreRiga`) VALUES
(1, 'Web', 'table-warning'),
(2, 'Arruzzoz', 'table-info'),
(3, 'wedwed', 'table-primary'),
(4, 'azzurro test', 'table-info'),
(5, 'blu', 'table-primary'),
(6, 'Cat1', 'table-info');

-- --------------------------------------------------------

--
-- Struttura della tabella `spese`
--

CREATE TABLE IF NOT EXISTS `spese` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `valore` float DEFAULT NULL,
  `descrizione` varchar(255) DEFAULT NULL,
  `categoria` varchar(32) DEFAULT NULL,
  `dataCreazione` date DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=45 ;

--
-- Dump dei dati per la tabella `spese`
--

INSERT INTO `spese` (`ID`, `valore`, `descrizione`, `categoria`, `dataCreazione`) VALUES
(18, 33, NULL, 'Benzina', NULL),
(17, 11, NULL, 'Bar', NULL),
(16, 11, NULL, 'Benzina', NULL),
(15, 1000.25, NULL, 'Benzina', NULL),
(14, 1000, NULL, 'Benzina', NULL),
(13, 1000, NULL, 'Benzina', NULL),
(12, 66, NULL, 'Benzina', NULL),
(19, 21, NULL, 'Benzina', NULL),
(20, 2233, NULL, 'Abarth', NULL),
(21, 88, NULL, 'Abarth', NULL),
(22, 1, NULL, 'Benzina', NULL),
(23, 88, NULL, 'Abarth', NULL),
(24, 11, 'ikekee', 'Benzina', NULL),
(25, 11, NULL, 'Benzina', '2019-09-27'),
(26, 88, NULL, 'Benzina', '2019-09-27'),
(27, 88, 'wkwk', 'Benzina', '2019-09-20'),
(28, 88, 'kwkw', 'Benzina', '2019-09-27'),
(29, 88, 'kwkw', 'Abarth', '2019-09-27'),
(30, 88, 'kwkw', 'Bar', '2019-09-27'),
(31, 88, 'kwkwkkk', 'Bar', '2019-09-27'),
(32, 88, 'djwedkewdkewd', 'Abarth', '2019-09-27'),
(33, 55, 'Ma ', 'Bar', '2019-09-12'),
(34, 88888, 'wkdkwddw', 'Benzina', '2019-09-27'),
(35, 99, 'wdknwd', 'Bar', '2019-09-27'),
(36, 99, 'wdknwd', 'Bar', '2019-09-26'),
(37, 99, 'acquisto coca', 'Bar', '2019-09-26'),
(38, 99, 'acquisto coca3', 'Bar', '2019-09-27'),
(39, 99, 'acquisto coca4', 'Abarth', '2019-09-27'),
(40, 99, 'acquisto coca4', 'Abarth', '2019-09-27'),
(41, 666666, 'dwede', 'table-info', '2019-10-04'),
(42, 449, 'blu', 'table-primary', '2019-10-04'),
(43, 56, NULL, 'wedwed', '2019-12-01'),
(44, 56, 'x regalo davide', 'blu', '2019-12-01');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
