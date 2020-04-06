(define (sqrt x)
	(sqrt-iter 1.0 x 0.0001))

(define (sqrt-iter guess x change)
	(if (good-enough? guess x change)
			guess
			(sqrt-iter (improve guess x)
								x
								(- guess change))))

(define (improve guess x)
	(average (guess (/ x guess))))

(define (average x y)
	(/ (+ x y) 2))

(define (good-enough? guess x change)
	())

(define (square x)
	(* x x))


