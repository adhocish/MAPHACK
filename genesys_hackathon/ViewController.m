//
//  ViewController.m
//  genesys_hackathon
//
//  Created by Alvin Xu on 9/26/15.
//  Copyright (c) 2015 Alvin Xu. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()


@end

@implementation ViewController
@synthesize label1, mytextview1, mytextview2;



- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any setup after loading the view, typically from a nib.
    
    UITapGestureRecognizer *tap = [[UITapGestureRecognizer alloc] initWithTarget:self
                                                                          action:@selector(dismissKeyboard)];
    
    [self.view addGestureRecognizer:tap];
    

}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

-(void)dismissKeyboard {
    [mytextview1 resignFirstResponder];
    [mytextview2 resignFirstResponder];
}



- (IBAction)showMessage
{
    /*
    UIAlertView *submitWorldAlert = [[UIAlertView alloc]
                                     initWithTitle:@"Test" message: @"submitted!" delegate:nil cancelButtonTitle:@"OK" otherButtonTitles:nil];
    [submitWorldAlert show];*/
    
    NSString *inputstring = [NSString stringWithFormat:@"%@%@%@", mytextview1.text, @"*", mytextview2.text];
    
    inputstring = [inputstring lowercaseString];
    
    
    NSCharacterSet *trim = [NSCharacterSet characterSetWithCharactersInString:@"0123456789abcdefghijklmnopqrstuvwxyz*.,;"];
    
    //NSString *dic = @"0123456789abcdefghijklmnopqrstuvwxyz*,;";
    
    trim = [trim invertedSet];
    NSString *result = [[inputstring componentsSeparatedByCharactersInSet:trim] componentsJoinedByString:@""];
    NSLog(@"%@", result);
    NSLog(@"%ld", result.length);
    
    
    
    
    NSString *currentchar = @"";
    //NSString *code =@"";
    NSString *encoded = @"";
    int mycount = 0;
    
    while(result.length > 0){
        currentchar = [result substringWithRange:NSMakeRange(0, 1)];
        NSLog(@"%@", currentchar);
        result = [result substringFromIndex:1];
        NSLog(@"%@", result);
        
        if([currentchar isEqualToString:@"0"]){
            encoded = [encoded stringByAppendingString:@"10"];
        }else if([currentchar isEqualToString:@"1"]){
            encoded = [encoded stringByAppendingString:@"11"];
        }else if([currentchar isEqualToString:@"2"]){
            encoded = [encoded stringByAppendingString:@"12"];
        }else if([currentchar isEqualToString:@"3"]){
            encoded = [encoded stringByAppendingString:@"13"];
        }else if([currentchar isEqualToString:@"4"]){
            encoded = [encoded stringByAppendingString:@"14"];
        }else if([currentchar isEqualToString:@"5"]){
            encoded = [encoded stringByAppendingString:@"15"];
        }else if([currentchar isEqualToString:@"6"]){
            encoded = [encoded stringByAppendingString:@"16"];
        }else if([currentchar isEqualToString:@"7"]){
            encoded = [encoded stringByAppendingString:@"17"];
        }else if([currentchar isEqualToString:@"8"]){
            encoded = [encoded stringByAppendingString:@"18"];
        }else if([currentchar isEqualToString:@"9"]){
            encoded = [encoded stringByAppendingString:@"19"];
        }else if([currentchar isEqualToString:@"a"]){
            encoded = [encoded stringByAppendingString:@"20"];
        }else if([currentchar isEqualToString:@"b"]){
            encoded = [encoded stringByAppendingString:@"21"];
        }else if([currentchar isEqualToString:@"c"]){
            encoded = [encoded stringByAppendingString:@"22"];
        }else if([currentchar isEqualToString:@"d"]){
            encoded = [encoded stringByAppendingString:@"23"];
        }else if([currentchar isEqualToString:@"e"]){
            encoded = [encoded stringByAppendingString:@"24"];
        }else if([currentchar isEqualToString:@"f"]){
            encoded = [encoded stringByAppendingString:@"25"];
        }else if([currentchar isEqualToString:@"g"]){
            encoded = [encoded stringByAppendingString:@"26"];
        }else if([currentchar isEqualToString:@"h"]){
            encoded = [encoded stringByAppendingString:@"27"];
        }else if([currentchar isEqualToString:@"i"]){
            encoded = [encoded stringByAppendingString:@"28"];
        }else if([currentchar isEqualToString:@"j"]){
            encoded = [encoded stringByAppendingString:@"29"];
        }else if([currentchar isEqualToString:@"k"]){
            encoded = [encoded stringByAppendingString:@"30"];
        }else if([currentchar isEqualToString:@"l"]){
            encoded = [encoded stringByAppendingString:@"31"];
        }else if([currentchar isEqualToString:@"m"]){
            encoded = [encoded stringByAppendingString:@"32"];
        }else if([currentchar isEqualToString:@"n"]){
            encoded = [encoded stringByAppendingString:@"33"];
        }else if([currentchar isEqualToString:@"o"]){
            encoded = [encoded stringByAppendingString:@"34"];
        }else if([currentchar isEqualToString:@"p"]){
            encoded = [encoded stringByAppendingString:@"35"];
        }else if([currentchar isEqualToString:@"q"]){
            encoded = [encoded stringByAppendingString:@"36"];
        }else if([currentchar isEqualToString:@"r"]){
            encoded = [encoded stringByAppendingString:@"37"];
        }else if([currentchar isEqualToString:@"s"]){
            encoded = [encoded stringByAppendingString:@"38"];
        }else if([currentchar isEqualToString:@"t"]){
            encoded = [encoded stringByAppendingString:@"39"];
        }else if([currentchar isEqualToString:@"u"]){
            encoded = [encoded stringByAppendingString:@"40"];
        }else if([currentchar isEqualToString:@"v"]){
            encoded = [encoded stringByAppendingString:@"41"];
        }else if([currentchar isEqualToString:@"w"]){
            encoded = [encoded stringByAppendingString:@"42"];
        }else if([currentchar isEqualToString:@"x"]){
            encoded = [encoded stringByAppendingString:@"43"];
        }else if([currentchar isEqualToString:@"y"]){
            encoded = [encoded stringByAppendingString:@"44"];
        }else if([currentchar isEqualToString:@"z"]){
            encoded = [encoded stringByAppendingString:@"45"];
        }else if([currentchar isEqualToString:@"*"]){
            encoded = [encoded stringByAppendingString:@"46"];
        }else if([currentchar isEqualToString:@"."]){
            encoded = [encoded stringByAppendingString:@"47"];
        }else if([currentchar isEqualToString:@","]){
            encoded = [encoded stringByAppendingString:@"48"];
        }else if([currentchar isEqualToString:@";"]){
            encoded = [encoded stringByAppendingString:@"49"];
        }
        
        mycount++;
       
    }
    encoded = [encoded stringByAppendingString:@"#"];
    NSLog(@"%@", encoded);
    
    label1.text = encoded;
    
    

 
    
    NSString *phoneNumber = @"18489993395";
    //NSString *groupNumber = @"08#";
    NSString *dtmfAfterPickup = encoded;
    //NSString *dtmfAfterPickup = [NSString stringWithFormat:@"%@%@", @"08#", encoded];
    
    
    
    NSString *telString = [NSString stringWithFormat:@"tel:%@,%@", phoneNumber, dtmfAfterPickup];
    [[UIApplication sharedApplication] openURL:[NSURL URLWithString:telString]];
  
    
}



@end
