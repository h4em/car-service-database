INSERT INTO status (id, name) 
VALUES 
    (1, 'COMPLETED'), 
    (2, 'CANCELLED'), 
    (3, 'IN PROGRESS'),
    (4, 'WAITING');

INSERT INTO position (id, name)
VALUES 
    (1, 'CEO'),
    (2, 'Service technician'),
    (3, 'Service advisor'),
    (4, 'Car mechanic'),
    (5, 'Car body technician'),
    (6, 'Quality control inspector'),
    (7, 'Parts manager'),
    (8, 'Service manager'),
    (9, 'Diagnostic technician'),
    (10, 'Detailer'),
    (11, 'Dispatcher'),
    (12, 'Sales and marketing specialist'),
    (13, 'Administrative assistant'),
    (14, 'Towing operator'),
    (15, 'Software technician'),
    (16, 'Custodian');

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

-- INSERT INTO employee (id, position_id, department_id, social_security_num, employment_date, leave_date)
-- VALUES 
--     (846, 1, 1, '79062820064', '2002-01-28', NULL),
--     (6, 16, 1, '22122236752', '2020-01-18', '2023-05-11'),
--     (8, 16, 1, '44061980136', '2006-09-27', NULL),
--     (11, 16, 1, '33050713572', '2012-06-25', NULL),
--     (13, 16, 1, '67043014674', '2004-03-01', NULL),
--     (14, 16, 2, '78090914183', '2021-09-22', NULL),
--     (15, 16, 2, '45050251600', '2018-07-24', NULL),
--     (17, 16, 2, '24111429248', '2004-09-25', NULL),
--     (18, 16, 2, '46073189200', '2012-04-06', '2018-10-29'),
--     (19, 16, 3, '87070432090', '2018-01-29', '2020-04-06'),
--     (20, 16, 3, '27042269956', '2012-12-20', NULL),
--     (22, 16, 3, '00271898607', '2021-01-17', '2022-01-27'),
--     (23, 16, 4, '30071049547', '2010-12-08', '2019-10-18'),
--     (24, 16, 4, '54011940473', '2008-12-04', '2013-11-07'),
--     (25, 16, 5, '85012950011', '2023-09-18', '2023-10-10'),
--     (28, 16, 5, '62022041926', '2006-11-15', NULL),
--     (29, 16, 6, '17062824923', '2003-04-02', NULL),
--     (30, 16, 7, '52120857552', '2017-08-23', NULL),
--     (31, 16, 8, '05122284581', '2017-07-04', NULL),
--     (33, 16, 9, '38061164526', '2016-06-10', NULL),
--     (35, 16, 10, '97092642447', '2021-12-16', NULL),
--     (36, 16, 11, '78060360073', '2003-03-13', NULL),
--     (37, 16, 12, '47070410836', '2002-03-02', NULL),
--     (38, 16, 13, '21100941493', '2013-11-06', '2019-12-16');

INSERT INTO Car (id, owner, license_plate, make, model, year) 
VALUES
    (614, 723, 'OO MFES1', 'MACK', 'CH', 2005),
    (615, 723, 'WO 0C4IP', 'FERRARI', 'FF', 2014),
    (616, 723, 'IP 5394Y', 'TOYOTA', '4RUNNER', 2012),
    (617, 806, 'IQ J48D4', 'SUZUKI', 'LT-A750X KINGQUAD AXI 4X4', 2008),
    (618, 806, 'KI 23HZ9', 'DUCATI', '1098', 2007),
    (619, 478, 'SN LT1DX', 'POLARIS', 'SPORTSMAN 850 HO XP EPS', 2013),
    (620, 478, 'SW FXF91', 'HARLEY DAVIDSON', 'FXDWG DYNA WIDE GLIDE', 2013),
    (621, 391, 'NU 3R106', 'GMC', 'YUKON', 2003),
    (622, 391, 'DJ 21R9A', 'TRIUMPH', 'TIGER 800 XC ABS', 2012),
    (623, 219, 'UE 890U9', 'BMW', 'K1200LT', 2001),
    (624, 219, 'EY T7609', 'YAMAHA', 'RS90MS RS VECTOR MOUNTAIN SE', 2006),
    (625, 137, 'UK CQ5I6', 'MINI', 'COOPER PACEMAN', 2014),
    (626, 137, 'KU 20196', 'HINO', '238', 2010),
    (627, 222, 'AC O447B', 'CAN-AM', 'RENEGADE 800R EFI X XC', 2012);