(define (cal a b)
	(if (> a b)
			0
			(+ (/ 1 (+ a (+ a 2)))
				 (cal (+ a 4) b))))
