(define (average x y)
	(/ (+ x y) 2))

(define (abs x)
	(cond ((< x 0) (- x))
				(else x)))

(define (square x)
	(* x x))

(define (sqrt-iter guess x)
	(if (new-good-enough? guess (improve guess))
			guess
			(sqrt-iter (improve guess x))))

(define (improve guess x)
	(average guess (/ x guess)))

(define (new-good-enough? guess new-guess)
	(< (abs (/ (- guess new-guess) guess)) 
		0.001))

(define (sqrt x)
	(sqrt-iter 1.0 x))
