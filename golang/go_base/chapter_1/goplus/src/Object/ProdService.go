package Object

import "log"

type ProdService struct {
}

func NewProdService() *ProdService {
	return &ProdService{}
}

func (s *ProdService) Save() {
	log.Println("save product success")
}
