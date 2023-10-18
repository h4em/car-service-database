-- INSERT INTO status (id, name) 
-- VALUES 
--     (1, 'COMPLETED'), 
--     (2, 'CANCELLED'), 
--     (3, 'IN PROGRESS');

-- INSERT INTO position (id, name)
-- VALUES 
--     (1, 'CEO'),
--     (2, 'Service technician'),
--     (3, 'Service advisor'),
--     (4, 'Car mechanic'),
--     (5, 'Car body technician'),
--     (6, 'Quality control inspector'),
--     (7, 'Parts manager'),
--     (8, 'Service manager'),
--     (9, 'Diagnostic technician'),
--     (10, 'Detailer'),
--     (11, 'Dispatcher'),
--     (12, 'Sales and marketing specialist'),
--     (13, 'Administrative assistant'),
--     (14, 'Towing operator'),
--     (15, 'Software technician'),
--     (16, 'Custodian');

INSERT INTO service (id, name, price) 
VALUES 
    (1, 'Oil change', 30.00), 
    (2, 'Synthetic oil change', 65.50),
    (3, 'Tire rotation and balance', 50.00),
    (4, 'Tire replacement (per tire)', 90.00),
    (5, 'Brake pad replacement', 250.00),
    (6, 'Brake rotor replacement', 350.00),
    (7, 'General safety inspection', 25.00),
    (8, 'A/C recharge and repair', 150.00),
    (9, 'Battery replacement', 129.99),
    (10, 'Transmission fluid change', 90.75),
    (11, 'Transmission rebuild', 3000.00),
    (12, 'Diagnostic scan and code reading', 75.00),
    (13, 'Engine performance check', 80.00),
    (14, 'Wheel alignment', 110.00),
    (15, 'Alternator replacement', 290.00),
    (16, 'Exhaust system repair or replacement', 190.00),
    (17, 'Basic interior and exterior detailing', 175.20),
    (18, 'Windshield repair', 60.00),
    (19, 'Windshield replacement', 250.00),
    (20, 'Towing service (per km)', 5.00);