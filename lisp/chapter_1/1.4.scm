
(define (compare a b c)
	(define x (+ a b))
	(define y (+ a c))
	(define z (+ b c))
	(if (> (compare-2 x y) z) 
			(compare-2 x y)
			z
	))

(define (compare-2 x y)
	(if (> x y ) x 
			y)
	)
