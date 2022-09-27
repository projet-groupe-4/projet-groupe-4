<?php

// Connexion a la BDD
$connexion = new PDO ('mysql:host=db;dbname=presentation','admin','admin');

// On va chercher l'entrer dans la bdd
$search = stripslashes($_POST["titre"]);
$requete = $connexion->query("SELECT * FROM articles WHERE titre like '".$search."'");

// On affiche le resultat
echo "Voici les resultats pour " .$search. " :";
while($data = $requete->fetch()){
        echo "<h1>".$data['titre']."</h1>";
        echo "<p>".$data['texte']."</p>";
}

// On tue kill la  requete
$requete->closeCursor();

?>

