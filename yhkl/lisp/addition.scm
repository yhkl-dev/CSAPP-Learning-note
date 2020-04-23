(define (+ x y)
	(if (= x 0)
			y
			(+ (- x 1) (+ 1 y))))
