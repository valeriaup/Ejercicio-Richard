<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, PUT, DELETE');

$productos = [
    [
        'id' => 1,
        'nombre' => 'Laptop',
        'precio' => 2500000
    ],
    [
        'id' => 2,
        'nombre' => 'Mouse',
        'precio' => 45000
    ],
    [
        'id' => 3,
        'nombre' => 'Teclado',
        'precio' => 120000
    ]
];

$metodo = $_SERVER['REQUEST_METHOD'];
$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$uri = explode('/', trim($uri, '/'));

switch ($metodo) {

    case 'GET':
        if (isset($uri[1]) && is_numeric($uri[1])) {
            $id = (int)$uri[1];
            $producto = array_filter($productos, fn($p) => $p['id'] === $id);

            echo json_encode(
                $producto
                    ? array_values($producto)[0]
                    : ['mensaje' => 'Producto no encontrado']
            );
        } else {
            echo json_encode($productos);
        }
        break;

    case 'POST':
        $input = json_decode(file_get_contents('php://input'), true);

        $nuevo = [
            'id' => count($productos) + 1,
            'nombre' => $input['nombre'] ?? '',
            'precio' => $input['precio'] ?? 0
        ];

        $productos[] = $nuevo;
        echo json_encode($nuevo);
        break;

    case 'PUT':
        $id = (int)($uri[1] ?? 0);
        $input = json_decode(file_get_contents('php://input'), true);

        foreach ($productos as &$p) {
            if ($p['id'] === $id) {
                $p['nombre'] = $input['nombre'] ?? $p['nombre'];
                $p['precio'] = $input['precio'] ?? $p['precio'];

                echo json_encode($p);
                exit;
            }
        }

        echo json_encode(['mensaje' => 'Producto no encontrado']);
        break;

    case 'DELETE':
        $id = (int)($uri[1] ?? 0);

        foreach ($productos as $i => $p) {
            if ($p['id'] === $id) {
                array_splice($productos, $i, 1);
                echo json_encode($p);
                exit;
            }
        }

        echo json_encode(['mensaje' => 'Producto no encontrado']);
        break;

    default:
        echo json_encode(['mensaje' => 'Metodo no permitido']);
}
?>