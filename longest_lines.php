#!/usr/bin/php
<?php
/*
Copyright © 2016 Dominique Barton

This file is part of Dominique Barton's CodeEval solutions.

Dominique Barton's CodeEval solutions are free software: you can redistribute
it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License,
or any later version.

Dominique Barton's CodeEval solutions are distributed in the hope that it
will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License
along with Dominique Barton's CodeEval solutions. If not, see
<http://www.gnu.org/licenses/>.

--------------------------------------------------------------------------------

Solution for the CodeEval challenge "Longest Lines":
https://www.codeeval.com/open_challenges/2/
*/

$f  = fopen($argv[1], "r");
$c  = fgets($f);
$ls = array();

while($l = fgets($f))
{
    $ls[strlen($l)] = trim($l);
}

ksort($ls, SORT_NUMERIC);

for($i=0; $i<$c; $i++)
    echo(array_pop($ls).PHP_EOL);

?>
