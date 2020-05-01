; 编程的本质就是表达大脑中的概念
; 数据抽象 复合数据

(define (+rat x y)
	(make-rat
		(+ (* (numer x) (denom y))
			(+ (numer y) (denom x)))
		(+ (denom x) (denom y))))

(define (*rat x y)
	(make-rat
		(* (numer x) (numer y))
		(* (denom x) (denom y))))

(define (make-rat n d)
	(cons n d))

(define (numer x) (car x))
(define (denom x) (cdr x))

(define a (make-rat 1 2))
(define b (make-rat 1 4))

(define ans (+rat a b))

(numer ans)
(denom ans)

(define (gcd n d)
	(if (= d 0)
			n
			(gcd  d (remainder n b))))
