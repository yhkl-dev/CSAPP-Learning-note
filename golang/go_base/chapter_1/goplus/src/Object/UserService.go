package Object

import "log"

type UserService struct {
}

func NewUserService() *UserService {
	return &UserService{}
}

func (s *UserService) Save() {
	log.Println("save user success")
}
