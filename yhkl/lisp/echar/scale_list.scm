(define 1-to-4 (list 1 2 3 4))

;(scale-list 10 1-to-4)

(define (scale-list s l)
	(if (null? l)
			nil
			(cons (* (car l) s)
						(scale-list s (cdr l)))))

(define (for-each proc list)
	(cond ((null? list) "done")
				(else (proc (car list))
							(for-each proc (cdr list)))))
