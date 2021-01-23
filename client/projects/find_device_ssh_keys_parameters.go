// Code generated by go-swagger; DO NOT EDIT.

package projects

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"
	"github.com/go-openapi/strfmt"
)

// NewFindDeviceSSHKeysParams creates a new FindDeviceSSHKeysParams object
// with the default values initialized.
func NewFindDeviceSSHKeysParams() *FindDeviceSSHKeysParams {
	var ()
	return &FindDeviceSSHKeysParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewFindDeviceSSHKeysParamsWithTimeout creates a new FindDeviceSSHKeysParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewFindDeviceSSHKeysParamsWithTimeout(timeout time.Duration) *FindDeviceSSHKeysParams {
	var ()
	return &FindDeviceSSHKeysParams{

		timeout: timeout,
	}
}

// NewFindDeviceSSHKeysParamsWithContext creates a new FindDeviceSSHKeysParams object
// with the default values initialized, and the ability to set a context for a request
func NewFindDeviceSSHKeysParamsWithContext(ctx context.Context) *FindDeviceSSHKeysParams {
	var ()
	return &FindDeviceSSHKeysParams{

		Context: ctx,
	}
}

// NewFindDeviceSSHKeysParamsWithHTTPClient creates a new FindDeviceSSHKeysParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewFindDeviceSSHKeysParamsWithHTTPClient(client *http.Client) *FindDeviceSSHKeysParams {
	var ()
	return &FindDeviceSSHKeysParams{
		HTTPClient: client,
	}
}

/*FindDeviceSSHKeysParams contains all the parameters to send to the API endpoint
for the find device SSH keys operation typically these are written to a http.Request
*/
type FindDeviceSSHKeysParams struct {

	/*SearchString
	  Search by key, label, or fingerprint

	*/
	SearchString *string
	/*ID
	  Project UUID

	*/
	ID strfmt.UUID
	/*Include
	  related attributes to include

	*/
	Include *string

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the find device SSH keys params
func (o *FindDeviceSSHKeysParams) WithTimeout(timeout time.Duration) *FindDeviceSSHKeysParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the find device SSH keys params
func (o *FindDeviceSSHKeysParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the find device SSH keys params
func (o *FindDeviceSSHKeysParams) WithContext(ctx context.Context) *FindDeviceSSHKeysParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the find device SSH keys params
func (o *FindDeviceSSHKeysParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the find device SSH keys params
func (o *FindDeviceSSHKeysParams) WithHTTPClient(client *http.Client) *FindDeviceSSHKeysParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the find device SSH keys params
func (o *FindDeviceSSHKeysParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithSearchString adds the searchString to the find device SSH keys params
func (o *FindDeviceSSHKeysParams) WithSearchString(searchString *string) *FindDeviceSSHKeysParams {
	o.SetSearchString(searchString)
	return o
}

// SetSearchString adds the searchString to the find device SSH keys params
func (o *FindDeviceSSHKeysParams) SetSearchString(searchString *string) {
	o.SearchString = searchString
}

// WithID adds the id to the find device SSH keys params
func (o *FindDeviceSSHKeysParams) WithID(id strfmt.UUID) *FindDeviceSSHKeysParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the find device SSH keys params
func (o *FindDeviceSSHKeysParams) SetID(id strfmt.UUID) {
	o.ID = id
}

// WithInclude adds the include to the find device SSH keys params
func (o *FindDeviceSSHKeysParams) WithInclude(include *string) *FindDeviceSSHKeysParams {
	o.SetInclude(include)
	return o
}

// SetInclude adds the include to the find device SSH keys params
func (o *FindDeviceSSHKeysParams) SetInclude(include *string) {
	o.Include = include
}

// WriteToRequest writes these params to a swagger request
func (o *FindDeviceSSHKeysParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	if o.SearchString != nil {

		// query param Search string
		var qrSearchString string
		if o.SearchString != nil {
			qrSearchString = *o.SearchString
		}
		qSearchString := qrSearchString
		if qSearchString != "" {
			if err := r.SetQueryParam("Search string", qSearchString); err != nil {
				return err
			}
		}

	}

	// path param id
	if err := r.SetPathParam("id", o.ID.String()); err != nil {
		return err
	}

	if o.Include != nil {

		// query param include
		var qrInclude string
		if o.Include != nil {
			qrInclude = *o.Include
		}
		qInclude := qrInclude
		if qInclude != "" {
			if err := r.SetQueryParam("include", qInclude); err != nil {
				return err
			}
		}

	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
