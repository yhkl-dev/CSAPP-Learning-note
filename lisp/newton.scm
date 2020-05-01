(define (sqrt x)
	(newton (lambda y) (- x (square y))
					1))

(define (newton f guess)
	(define df (deriv f))
	(fixed-point 
		(lambda (x) (- x (/ (f x) (df x))))
		guess)

(define deriv
	(lambda (f)
		(lambda (x) (/ (- f (+ x dx)
											(f x))
									 dx))))
