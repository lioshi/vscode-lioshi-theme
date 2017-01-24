<?php

include "classes.inc";

// classe de base, avec des propriétés et des méthodes membres
class Vegetable {
    var $edible;
    var $color;

    function Vegetable($edible, $color="green") 
    {
        $this->edible = $edible;
        $this->color = $color;
    }

    function is_edible() 
    {
        return $this->edible;
    }

    function class_parentage($obj, $class) 
    {
        if (is_subclass_of($GLOBALS[$obj], $class)) {
            echo "L'objet $obj appartient à la classe " . get_class($$obj);
            echo " une sous-classe de $class\n";
        } else {
            echo "L'object $obj n'appartient pas à une sous-classe $class\n";
        }
    }

} // fin de la classe Vegetable


