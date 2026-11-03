INSERT INTO books (id, title, author, price, publisher, image_path, like_count) VALUES (1, 'Pythonの教科書', '山田 太郎', 2500, '技術書院', '/images/1.png', 0);
INSERT INTO books (id, title, author, price, publisher, image_path, like_count) VALUES (2, 'Vue.js入門', '山田 太郎', 3000, '技術評論社', '/images/2.png', 0);
INSERT INTO books (id, title, author, price, publisher, image_path, like_count) VALUES (3, 'Django開発', '佐藤 健一', 2800, '技術評論社', '/images/3.png', 0);
INSERT INTO books (id, title, author, price, publisher, image_path, like_count) VALUES (4, 'JavaScript完全', '山田 太郎', 3200, '技術評論社', '/images/4.png', 0);
INSERT INTO books (id, title, author, price, publisher, image_path, like_count) VALUES (5, 'AIの基礎', '田中 未来', 3500, '未来技術社', '/images/5.png', 0);
INSERT INTO books (id, title, author, price, publisher, image_path, like_count) VALUES (6, 'React実践', '伊藤 さくら', 3100, '技術評論社', '/images/6.png', 0);
INSERT INTO books (id, title, author, price, publisher, image_path, like_count) VALUES (7, 'Go言語', '渡辺 剛', 3400, '技術評論社', '/images/7.png', 0);
INSERT INTO books (id, title, author, price, publisher, image_path, like_count) VALUES (8, 'Docker活用', '山田 太郎', 2900, 'クラウド書房', '/images/8.png', 0);
INSERT INTO books (id, title, author, price, publisher, image_path, like_count) VALUES (9, 'AWS構築', '山田 太郎', 3800, 'インフラ技術社', '/images/9.png', 0);
INSERT INTO books (id, title, author, price, publisher, image_path, like_count) VALUES (10, 'アジャイル', '吉田 チーム', 2600, 'J-TECH', '/images/10.png', 0);

SELECT * FROM books ORDER BY id;
