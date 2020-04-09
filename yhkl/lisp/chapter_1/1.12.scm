(define (pascal n)
	(pascal-iter n 1))


(define (pascal-iter n data)
	(if (= n 1)
			(list data)
