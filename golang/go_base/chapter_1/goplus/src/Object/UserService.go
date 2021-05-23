package Object

import "log"

type UserService struct {
}

func NewUserService() *UserService {
	return &UserService{}
}

func (s *UserService) Save(data interface{}) IService {
	if user, ok := data.(*User); ok {
		log.Printf("%v\n", user)
		log.Println("save user success")
	} else {
		log.Fatal("user attr error")
	}
	return s
}

func (s *UserService) List() IService {
	log.Println("list user lists")
	return s
}
