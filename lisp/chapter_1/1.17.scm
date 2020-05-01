;(define (* a b)
;  (if (= b 0)
;      0
;      (+ a (* a (- b 1))))
;  )

(define (double x)
  (+ x x )
  )

(define (halve x)
  (/ x 2)
  )


(define (expt-new a b)
  (cond ((= b 0 ) 0)
	(else (+ (double a) (* (double a) (- (halve b) 1))) )))
