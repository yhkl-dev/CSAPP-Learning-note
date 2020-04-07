(define (square x)
	(* x x )
	)

(define (cube x)
	(* x x x))

(define (sqrt-3 x)
	(sqrt-iter 1.0 x)
	)

(define (sqrt-iter guess x)
	(if (good-enough? guess x)
			guess
			(sqrt-iter (improve guess x) x)))


(define (improve guess x)
	(/ (+ (/ x (square guess)) (* 2 guess)) 3))

(define (good-enough? guess x)
	(< (abs (- (cube guess) x)) 0.001))

(define (abs x)
	(cond ((< x 0) (x) )
				(- x)))
