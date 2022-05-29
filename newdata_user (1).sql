-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.2:3307
-- Generation Time: May 29, 2022 at 08:13 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `newdata_user`
--

-- --------------------------------------------------------

--
-- Table structure for table `likedmovie`
--

CREATE TABLE `likedmovie` (
  `id` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `moviename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `likedmovie`
--

INSERT INTO `likedmovie` (`id`, `email`, `moviename`) VALUES
(2, 'ishwar@gmail.com', 'avatar'),
(3, 'ishwar@gmail.com', 'the namesake'),
(4, 'ishwar@gmail.com', 'jack the giant slayer'),
(5, 'ishwar@gmail.com', 'harry potter and the prisoner of azkaban'),
(6, 'ishwar@gmail.com', 'now you see me 2'),
(7, 'paaji@gmail.com', 'avatar'),
(8, 'ishwar@gmail.com', 'the expendables 3'),
(9, 'ishwar@gmail.com', 'the best of me'),
(10, 'harshsengar@gmail.com', 'warcraft'),
(11, 'harshsengar@gmail.com', 'john carter'),
(12, 'harshsengar@gmail.com', 'raising cain'),
(13, 'harshsengar@gmail.com', 'avatar'),
(14, 'harshsengar@gmail.com', 'tears of the sun'),
(15, 'harshsengar@gmail.com', 'zero dark thirty'),
(16, 'harshsengar@gmail.com', 'act of valor'),
(17, 'harshsengar@gmail.com', 'the dark knight'),
(18, 'harshsengar@gmail.com', 'thor'),
(19, 'prem@gmail.com', 'warcraft'),
(20, 'avengers@gmail.com', 'titanic'),
(21, 'avengers@gmail.com', 'the switch'),
(22, 'harshdev12@gmail.com', 'spectre'),
(23, 'harshdev12@gmail.com', 'never say never again'),
(24, 'harshdev12@gmail.com', 'avatar'),
(25, 'harshdev12@gmail.com', 'the avengers'),
(26, 'harshdev12@gmail.com', 'avengers: age of ultron'),
(27, 'harshdev12@gmail.com', 'superman returns'),
(28, 'harshdev12@gmail.com', 'inside out'),
(29, 'harshdev12@gmail.com', 'thor');

-- --------------------------------------------------------

--
-- Table structure for table `search_history`
--

CREATE TABLE `search_history` (
  `id` int(11) NOT NULL,
  `movieid` int(11) NOT NULL,
  `moviename` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `search_history`
--

INSERT INTO `search_history` (`id`, `movieid`, `moviename`, `email`) VALUES
(1, 10195, 'thor', 'ishwar@gmail.com'),
(2, 19995, 'avatar', 'paaji@gmail.com'),
(3, 19995, 'avatar', 'paaji@gmail.com'),
(4, 19995, 'avatar', 'paaji@gmail.com'),
(5, 68735, 'warcraft', 'paaji@gmail.com'),
(6, 49521, 'man of steel', 'paaji@gmail.com'),
(7, 49521, 'man of steel', 'paaji@gmail.com'),
(8, 49521, 'man of steel', 'paaji@gmail.com'),
(9, 49521, 'man of steel', 'paaji@gmail.com'),
(10, 49521, 'man of steel', 'paaji@gmail.com'),
(11, 49521, 'man of steel', 'paaji@gmail.com'),
(12, 49521, 'man of steel', 'paaji@gmail.com'),
(13, 49521, 'man of steel', 'paaji@gmail.com'),
(14, 49521, 'man of steel', 'paaji@gmail.com'),
(15, 49521, 'man of steel', 'paaji@gmail.com'),
(16, 49521, 'man of steel', 'paaji@gmail.com'),
(17, 49521, 'man of steel', 'paaji@gmail.com'),
(18, 49521, 'man of steel', 'paaji@gmail.com'),
(19, 49521, 'man of steel', 'paaji@gmail.com'),
(20, 49521, 'man of steel', 'paaji@gmail.com'),
(21, 49521, 'man of steel', 'paaji@gmail.com'),
(22, 49521, 'man of steel', 'paaji@gmail.com'),
(23, 10195, 'thor', 'ishwar@gmail.com'),
(24, 76338, 'thor: the dark world', 'ishwar@gmail.com'),
(25, 68735, 'warcraft', 'ishwar@gmail.com'),
(26, 138103, 'the expendables 3', 'ishwar@gmail.com'),
(27, 138103, 'the expendables 3', 'ishwar@gmail.com'),
(28, 138103, 'the expendables 3', 'ishwar@gmail.com'),
(29, 13569, 'thr3e', 'ishwar@gmail.com'),
(30, 10195, 'thor', 'ishwar@gmail.com'),
(31, 33155, 'galaxina', 'ishwar@gmail.com'),
(32, 10195, 'thor', 'ishwar@gmail.com'),
(33, 76338, 'thor: the dark world', 'ishwar@gmail.com'),
(34, 658, 'goldfinger', 'ishwar@gmail.com'),
(35, 81005, 'jack the giant slayer', 'ishwar@gmail.com'),
(36, 267935, 'the bfg', 'ishwar@gmail.com'),
(37, 11631, 'mamma mia!', 'ishwar@gmail.com'),
(38, 239571, 'the best of me', 'ishwar@gmail.com'),
(39, 137347, 'closer to the moon', 'ishwar@gmail.com'),
(40, 68735, 'warcraft', 'ishwar@gmail.com'),
(41, 81005, 'jack the giant slayer', 'ishwar@gmail.com'),
(42, 29427, 'the crazies', 'ishwar@gmail.com'),
(43, 49026, 'the dark knight rises', 'ishwar@gmail.com'),
(44, 16727, 'the namesake', 'ishwar@gmail.com'),
(45, 267935, 'the bfg', 'ishwar@gmail.com'),
(46, 12610, 'osmosis jones', 'ishwar@gmail.com'),
(47, 239571, 'the best of me', 'ishwar@gmail.com'),
(48, 10733, 'the alamo', 'ishwar@gmail.com'),
(49, 76493, 'the dictator', 'ishwar@gmail.com'),
(50, 76493, 'the dictator', 'ishwar@gmail.com'),
(51, 159037, 'the square', 'ishwar@gmail.com'),
(52, 11622, 'blast from the past', 'ishwar@gmail.com'),
(53, 2619, 'splash', 'ishwar@gmail.com'),
(54, 68735, 'warcraft', 'harshsengar@gmail.com'),
(55, 4723, 'southland tales', 'harshsengar@gmail.com'),
(56, 4723, 'southland tales', 'harshsengar@gmail.com'),
(57, 4723, 'southland tales', 'harshsengar@gmail.com'),
(58, 4723, 'southland tales', 'harshsengar@gmail.com'),
(59, 72976, 'lincoln', 'harshsengar@gmail.com'),
(60, 72976, 'lincoln', 'harshsengar@gmail.com'),
(61, 72976, 'lincoln', 'harshsengar@gmail.com'),
(62, 49529, 'john carter', 'harshsengar@gmail.com'),
(63, 13937, 'raising cain', 'harshsengar@gmail.com'),
(64, 13937, 'raising cain', 'harshsengar@gmail.com'),
(65, 19995, 'avatar', 'harshsengar@gmail.com'),
(66, 9567, 'tears of the sun', 'harshsengar@gmail.com'),
(67, 352978, 'chain of command', 'harshsengar@gmail.com'),
(68, 352978, 'chain of command', 'harshsengar@gmail.com'),
(69, 97630, 'zero dark thirty', 'harshsengar@gmail.com'),
(70, 75674, 'act of valor', 'harshsengar@gmail.com'),
(71, 1852, 'world trade center', 'harshsengar@gmail.com'),
(72, 155, 'the dark knight', 'harshsengar@gmail.com'),
(73, 10195, 'thor', 'harshsengar@gmail.com'),
(74, 68735, 'warcraft', 'prem@gmail.com'),
(75, 49529, 'john carter', 'prem@gmail.com'),
(76, 10195, 'thor', 'ishwar@gmail.com'),
(77, 1250, 'ghost rider', 'avengers@gmail.com'),
(78, 597, 'titanic', 'avengers@gmail.com'),
(79, 49529, 'john carter', 'avengers@gmail.com'),
(80, 767, 'harry potter and the half-blood prince', 'avengers@gmail.com'),
(81, 41210, 'the switch', 'avengers@gmail.com'),
(82, 1259, 'notes on a scandal', 'avengers@gmail.com'),
(83, 559, 'spider-man 3', 'avengers@gmail.com'),
(84, 206647, 'spectre', 'avengers@gmail.com'),
(85, 38757, 'tangled', 'avengers@gmail.com'),
(86, 102382, 'the amazing spider-man 2', 'avengers@gmail.com'),
(87, 206647, 'spectre', 'harshdev12@gmail.com'),
(88, 49026, 'the dark knight rises', 'harshdev12@gmail.com'),
(89, 76338, 'thor: the dark world', 'harshdev12@gmail.com'),
(90, 608, 'men in black ii', 'harshdev12@gmail.com'),
(91, 608, 'men in black ii', 'harshdev12@gmail.com'),
(92, 36670, 'never say never again', 'harshdev12@gmail.com'),
(93, 19995, 'avatar', 'harshdev12@gmail.com'),
(94, 1250, 'ghost rider', 'harshdev12@gmail.com'),
(95, 24428, 'the avengers', 'harshdev12@gmail.com'),
(96, 99861, 'avengers: age of ultron', 'harshdev12@gmail.com'),
(97, 41154, 'men in black 3', 'harshdev12@gmail.com'),
(98, 1452, 'superman returns', 'harshdev12@gmail.com'),
(99, 150540, 'inside out', 'harshdev12@gmail.com'),
(100, 1591, 'nowhere in africa', 'harshdev12@gmail.com'),
(101, 10195, 'thor', 'harshdev12@gmail.com'),
(102, 767, 'harry potter and the half-blood prince', 'harshdev12@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `uname` varchar(25) NOT NULL,
  `umail` varchar(25) NOT NULL,
  `uphone` varchar(14) NOT NULL,
  `upass` varchar(30) NOT NULL,
  `cupass` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `uname`, `umail`, `uphone`, `upass`, `cupass`) VALUES
(5, 'avengers', 'ishwar@gmail.com', '3454654565', '1234', '1234'),
(6, 'thor', 'avengers@gmail.com', '1234590098', '1234', '1234'),
(7, 'Harsh ', 'harshdev@gmail.com', '123456789', '12345', '12345'),
(8, 'HARSH', 'harshdev12@gmail.com', '2414243434', '123456', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `user_rating`
--

CREATE TABLE `user_rating` (
  `id` int(11) NOT NULL,
  `id_user` varchar(11) NOT NULL,
  `movieid` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_rating`
--

INSERT INTO `user_rating` (`id`, `id_user`, `movieid`, `rating`, `email`) VALUES
(1, '1', 4, 81005, 'ishwar@gmail.com'),
(2, '1', 9, 137347, 'ishwar@gmail.com'),
(3, '2', 4, 19995, 'paaji@gmail.com'),
(4, '1', 4, 138103, 'ishwar@gmail.com'),
(5, '1', 8, 239571, 'ishwar@gmail.com'),
(6, '1', 8, 68735, 'ishwar@gmail.com'),
(7, '1', 8, 29427, 'ishwar@gmail.com'),
(8, '3', 6, 68735, 'harshsengar@gmail.com'),
(9, '3', 6, 4723, 'harshsengar@gmail.com'),
(10, '6', 6, 597, 'avengers@gmail.com'),
(11, '6', 6, 767, 'avengers@gmail.com'),
(12, '6', 5, 41210, 'avengers@gmail.com'),
(13, '8', 9, 608, 'harshdev12@gmail.com'),
(14, '8', 8, 41154, 'harshdev12@gmail.com'),
(15, '8', 6, 1452, 'harshdev12@gmail.com'),
(16, '8', 2, 767, 'harshdev12@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `likedmovie`
--
ALTER TABLE `likedmovie`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `search_history`
--
ALTER TABLE `search_history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_rating`
--
ALTER TABLE `user_rating`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `likedmovie`
--
ALTER TABLE `likedmovie`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `search_history`
--
ALTER TABLE `search_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=103;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `user_rating`
--
ALTER TABLE `user_rating`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
