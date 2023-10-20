<?php
header('Content-Type: application/json');

// Goat database (in-memory for simplicity)
$goats = [];

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    echo json_encode($goats);
} elseif ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    array_push($goats, $data);
    echo json_encode(['message' => 'Goat added successfully']);
}
?>
