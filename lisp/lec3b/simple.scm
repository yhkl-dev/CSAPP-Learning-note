(define deriv
	(lambda (f)
		(lambda (x)
			(/ (- (f (+ x dx))
						(f x))
				 dx))))
