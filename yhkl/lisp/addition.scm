;(define (+ x y)
;	(if (= x 0)
;			y
;			(+ (- x 1) (+ 1 y))))

(define (plus x y)
	(if (= x 0)
			y
			(plus 1 (plus (- x 1) y))))
