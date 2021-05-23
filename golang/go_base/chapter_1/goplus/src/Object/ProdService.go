package Object

import "log"

type ProdService struct {
}

func NewProdService() *ProdService {
	return &ProdService{}
}

func (s *ProdService) Save(data interface{}) IService {
	log.Println("save product success")
	return s
}

func (s *ProdService) List() IService {
	log.Println("list product lists")
	return s
}
