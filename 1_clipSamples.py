import numpy as np
import pandas as pd
import rasterio as rio
import affine

#class to manage image clipping(need image address and entity-row-column dataset,band_no to proceed)
class ClipImage:

    # Get band, band shape, dtype, crs and transform values
    def __init__(self, image_address,df,bandNo):
        with rio.open(image_address, 'r') as f:
            self.band = f.read(bandNo)
            self.crs = f.crs
            self.b_trans = f.transform
        self.bNo = bandNo
        self.dataset=df
        self.r = df.iloc[:,1]
        self.c = df.iloc[:,2]
        self.entity = df.iloc[:,0]
        self.Ttype = df.iloc[:,3]
        self.band_shape = self.band.shape
        self.band_dtype = self.band.dtype
        self.clipped_images = []
        self.clipped_addresses = []

    # Function for clipping band
    def clip_raster(self, height, width, buffer=0,
                    save_mode=False, prefix='clipped_band_', 
                    pass_empty=False):
        height = height/2
        width = width/2
        for i in range(0,len(self.dataset)):
            r_pos = self.r[i]
            col_pos = self.c[i]
            xmin = int(r_pos-height)
            xmax = int(r_pos+height)
            ymin = int(col_pos-width)
            ymax = int(col_pos+width)              
            clipped_image = self.band[xmin:xmax,ymin:ymax]

            # Check if frame is empty
            if pass_empty:
                if np.mean(clipped_image) == 0:
                    print('Empty frame, not saved')
                    break

            # Positioning
            tcol, trow = self.b_trans*(col_pos-width, r_pos-height)
            new_transform = affine.Affine(self.b_trans[0], 
                                            self.b_trans[1],
                                            tcol,
                                            self.b_trans[3], 
                                            self.b_trans[4], 
                                            trow)
            image = [clipped_image, self.crs, new_transform,
                        clipped_image.shape[0], 
                        clipped_image.shape[1],
                        self.band_dtype]

            # Save or append into a set
            if save_mode:
                filename = prefix + f"{self.Ttype[i]}_{self.entity[i]}_{i+1}_b_{self.bNo}.tif"

                with rio.open(filename, 'w',
                                driver='GTiff',
                                height=image[3], width=image[4],
                                count=1, dtype=image[5],
                                crs=image[1],
                                transform=image[2]) as dst:
                    dst.write(image[0], 1)
                self.clipped_addresses.append(filename)
            else:
                self.clipped_images.append(clipped_image)

        if save_mode:
            print('Tiles saved successfully')
            return self.clipped_addresses
        else:
            print('Tiles prepared successfully')
            return self.clipped_images

#create entity-row-col dataframe using csv file
data = pd.read_csv("points.csv")
data = data[['entity','Row','Col','type']]
print('Preview of the imported dataset\n\n',data.head(),'\n')

#executing the method created
path = 'Cropped/Cropped1.tif'
for no in range(1,5):
    clipper = ClipImage(image_address=path,df=data,bandNo=no)
    clipper.clip_raster(height=20,
        width=20,
        buffer=0,
        save_mode=True,
        prefix="samples/",
        pass_empty=False)