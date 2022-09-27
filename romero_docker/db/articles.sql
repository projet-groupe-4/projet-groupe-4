-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Client :  localhost:3306
-- Généré le :  Jeu 19 Décembre 2019 à 14:06
-- Version du serveur :  10.1.26-MariaDB-0+deb9u1
-- Version de PHP :  7.0.30-0+deb9u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `presentation`
--

-- --------------------------------------------------------

--
-- Structure de la table `articles`
--

CREATE TABLE `articles` (
  `id` int(4) NOT NULL,
  `titre` varchar(50) NOT NULL,
  `auteur` varchar(20) NOT NULL,
  `texte` text NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Contenu de la table `articles`
--

INSERT INTO `articles` (`id`, `titre`, `auteur`, `texte`, `date`) VALUES
(1, 'GetSploit V0.2.2', 'Florian', 'Cet outil vous permet de rechercher en ligne pour des exploits parmi de nombreuses bases telles que :\r\n\r\nExploit-DB\r\nMetasploit\r\nPacketstorm\r\net bien d’autres', '2018-09-25'),
(3, 'Shodan – Contrôler des imprimantes 3D Octoprint', 'Alexis', 'La technologie de l’impression 3D est en plein essor ! Il existe de nombreuses marques et technologies gravitant autour de ça.\r\n\r\n\r\nIl existe une interface web nommée Octoprint, qui permet d’accéder à l’interface d’impression des machines 3D. Grâce à notre outil préféré Shodan, il est alors possible de déceler les interfaces accessibles.', '2018-09-25'),
(4, 'Liens en vrac', 'Jack', 'Les liens ci-dessous sont des liens partagés en conversation  et sont donc à trier:\r\n\r\nhttps://kalilinuxtutorials.com/getsploit-searching-downloading-exploits/\r\nhttps://kalilinuxtutorials.com/spykeyboard-keylogger-sends-data-gmail/\r\nhttps://blog.scrt.ch/2018/08/24/remote-code-execution-on-a-facebook-server/\r\nhttps://www.newsletteraccess.com/\r\nhttps://www.smarttoolsshop.icu\r\nhttps://www.welivesecurity.com/2018/08/29/semi-annual-balance-mobile-security/\r\nhttps://github.com/Kickball/awesome-selfhosted/blob/master/README.md\r\nhttps://www.sken.io/\r\nhttps://github.com/Kickball/awesome-selfhosted/blob/master/README.md\r\nhttps://peek.link/\r\nhttps://atcommands.org/atdb/commands\r\nhttps://atcommands.org/atdb/\r\nhttps://www.01net.com/actualites/android-des-commandes-secretes-permettent-de-pirater-des-millions-de-smartphones-1512460.html\r\nhttps://korben.info/desactivez-les-fonctionnalites-a-risque-de-windows-avec-hardentools.html\r\nhttps://www.sken.io/', '2018-09-25');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `articles`
--
ALTER TABLE `articles`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `articles`
--
ALTER TABLE `articles`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
