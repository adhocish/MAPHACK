//
//  ViewController.h
//  genesys_hackathon
//
//  Created by Alvin Xu on 9/26/15.
//  Copyright (c) 2015 Alvin Xu. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController

@property (weak, nonatomic) IBOutlet UITextField *mytextview1;

@property (weak, nonatomic) IBOutlet UITextField *mytextview2;

@property (weak, nonatomic) IBOutlet UILabel *label1;

-(IBAction)showMessage;

@end

