(define (cube x)
	(* x x x))

(define (p x) (- (* 3 x) (*  4 (cube x))))

(define (sine angle)
	(if (not (> (abs angle) 0.1))
					 angle
					 (p (sine (/ angle 3.0)))))

; 在求值 (sine 12.15) 时，p被调用5次
; O(log a) 每次a增加3倍 p的调用次数增加1
