(define (deriv exp var)
	(cond ((constant? exp var) 0)
				((same-var? exp var) 1)
				((sum? exp)
				 (make-sum (deriv (A1 exp) var)
									 (deriv (A2 exp) var)))
				((product? exp)
				 (make-sum
					 (make-product (M1 exp)
												 (deriv (M2 exp) var))
					 (make-product (deriv (M1 exp) var)
												 (M2 exp))))))

(define (constant? exp var)
	(and (atom? exp)
			 (not (eq? exp var))))

(define (same-var? exp var)
	(and (atom? exp)
			 (eq? exp var)))

(define (sum? exp)
	(and (not (atom? exp))
			 (eq (car exp) '+)))

(define (make-sum A1 A2)
	(list '+ A1 A2))

(define A1 cadr)
(define A2 caddr)

(define (product? exp)
	(and (not (atom? exp))
			 (eq? (car exp) '*)))

(define (make-product M1 M2)
	(list '* M1 M2))

(define M1 cadr)
(define M2 caddr)

(define (make-sum A1 A2)
	(cond ((and (number? A1)
							(number? A2)
							)
				 (+ A1 A2))
				((and (number? A1) (= A1 0)) A2 )
				((and (number? A2) (= A2 0)) A1)
				(else (list '+ A1 A2))))
