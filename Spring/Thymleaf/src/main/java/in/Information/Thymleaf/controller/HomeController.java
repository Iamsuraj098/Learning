package in.Information.Thymleaf.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController{

    @GetMapping({"/", "/home", ""})
    public String showHomePage(Model model){
        model.addAttribute("title", "home");
        return "master";
    }

    @GetMapping({"/projects"})
    public String showProjectPage(Model model){
        model.addAttribute("title", "projects");
        return "master";
    }

    @GetMapping({"/resume"})
    public String showResumePage(Model model){
        model.addAttribute("title", "resume");
        return "master";
    }

    @GetMapping({"/contact"})
    public String showContactPage(Model model){
        model.addAttribute("title", "contact");
        return "master";
    }
}
