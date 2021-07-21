package main;

public class defangingAnIpAddress {
    public String defangIPaddr(String address) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < address.length(); i++) {
            if (address.charAt(i) == '.')
                sb.append("[.]");
            else
                sb.append(address.charAt(i));
        }
        return sb.toString();

    }
}

// 그냥 return address.replace(".", "[.]"); 해도 똑같음
